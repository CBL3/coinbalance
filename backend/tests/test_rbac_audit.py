from datetime import datetime, timedelta, timezone

import jwt
import pytest

from app import create_app
from app.config import Config
from app.core.audit import AuditEvent
from app.extensions import db
from app.modules.identity.models import Permission, Role, User
from app.modules.organizations.models import Organization


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = "test-secret-key-for-coinbalance-0-2"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def make_token(user: User) -> str:
    payload = {
        "sub": user.id,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15),
    }
    return jwt.encode(payload, TestConfig.SECRET_KEY, algorithm="HS256")


@pytest.fixture
def identity_fixture(app):
    org_a = Organization(legal_name="Tenant A", display_name="Tenant A")
    org_b = Organization(legal_name="Tenant B", display_name="Tenant B")

    audit_read = Permission(name="audit:read", description="Read audit trails")
    evidence_upload = Permission(name="evidence:upload", description="Upload evidence")
    reconciliation_read = Permission(name="reconciliation:read", description="Read reconciliation findings")
    reconciliation_run = Permission(name="reconciliation:run", description="Run reconciliation tasks")
    system_admin_permission = Permission(name="system:admin", description="System admin")

    auditor_role = Role(name="Auditor", organization=org_a)
    auditor_role.permissions.extend([audit_read, reconciliation_read])

    viewer_role = Role(name="Viewer", organization=org_a)

    admin_role = Role(name="System Administrator")
    admin_role.permissions.extend(
        [audit_read, evidence_upload, reconciliation_read, reconciliation_run, system_admin_permission]
    )

    auditor = User(
        organization=org_a,
        email="auditor@example.com",
        display_name="Auditor",
    )
    auditor.roles.append(auditor_role)

    viewer = User(
        organization=org_a,
        email="viewer@example.com",
        display_name="Viewer",
    )
    viewer.roles.append(viewer_role)

    admin = User(
        organization=org_a,
        email="admin@example.com",
        display_name="Admin",
    )
    admin.roles.append(admin_role)

    db.session.add_all(
        [
            org_a,
            org_b,
            audit_read,
            system_admin_permission,
            auditor_role,
            viewer_role,
            admin_role,
            auditor,
            viewer,
            admin,
        ]
    )
    db.session.flush()

    event_a = AuditEvent.record_event(
        organization_id=org_a.id,
        actor_id=auditor.id,
        event_type="identity.seeded",
        entity_type="organization",
        entity_id=org_a.id,
        metadata={"source": "test"},
    )
    event_b = AuditEvent.record_event(
        organization_id=org_b.id,
        actor_id=admin.id,
        event_type="identity.seeded",
        entity_type="organization",
        entity_id=org_b.id,
        metadata={"source": "test"},
    )
    db.session.commit()

    return {
        "org_a": org_a,
        "org_b": org_b,
        "auditor": auditor,
        "viewer": viewer,
        "admin": admin,
        "event_a": event_a,
        "event_b": event_b,
    }


def test_identity_me_requires_authentication(client):
    response = client.get("/api/v1/identity/me")

    assert response.status_code == 401


def test_identity_me_returns_authenticated_user(client, identity_fixture):
    auditor = identity_fixture["auditor"]

    response = client.get(
        "/api/v1/identity/me",
        headers={"Authorization": f"Bearer {make_token(auditor)}"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["email"] == "auditor@example.com"
    assert payload["organization_id"] == identity_fixture["org_a"].id
    assert payload["permissions"] == ["audit:read", "reconciliation:read"]


def test_audit_events_are_scoped_to_user_organization(client, identity_fixture):
    auditor = identity_fixture["auditor"]

    response = client.get(
        "/api/v1/audit/events",
        headers={"Authorization": f"Bearer {make_token(auditor)}"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert [event["id"] for event in payload["events"]] == [identity_fixture["event_a"].id]


def test_audit_events_reject_cross_organization_query(client, identity_fixture):
    auditor = identity_fixture["auditor"]
    org_b = identity_fixture["org_b"]

    response = client.get(
        f"/api/v1/audit/events?organization_id={org_b.id}",
        headers={"Authorization": f"Bearer {make_token(auditor)}"},
    )

    assert response.status_code == 403


def test_audit_events_require_permission(client, identity_fixture):
    viewer = identity_fixture["viewer"]

    response = client.get(
        "/api/v1/audit/events",
        headers={"Authorization": f"Bearer {make_token(viewer)}"},
    )

    assert response.status_code == 403


def test_system_admin_can_filter_any_organization(client, identity_fixture):
    admin = identity_fixture["admin"]
    org_b = identity_fixture["org_b"]

    response = client.get(
        f"/api/v1/audit/events?organization_id={org_b.id}",
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert [event["id"] for event in payload["events"]] == [identity_fixture["event_b"].id]
