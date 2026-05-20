from datetime import datetime, timedelta, timezone

import jwt

from app.core.audit import AuditEvent
from app.extensions import db
from app.modules.identity.models import Role, User
from app.modules.organizations.models import Organization
from app.modules.reconciliation.models import ReconciliationFinding
from app.modules.evidence.models import Evidence

from backend.tests.test_rbac_audit import app, client, identity_fixture, make_token


def test_evidence_upload_requires_permission(client, app):
    with app.app_context():
        org = Organization(legal_name="Tenant C", display_name="Tenant C")
        viewer_role = Role(name="Viewer", organization=org)
        viewer = User(
            organization=org,
            email="viewer@example.com",
            display_name="Viewer",
        )
        viewer.roles.append(viewer_role)
        db.session.add_all([org, viewer_role, viewer])
        db.session.commit()

        response = client.post(
            "/api/v1/evidence",
            json={
                "title": "Sample Evidence",
                "sha256_hash": "0" * 64,
                "storage_uri": "s3://bucket/evidence.json",
            },
            headers={"Authorization": f"Bearer {make_token(viewer)}"},
        )

        assert response.status_code == 403


def test_evidence_upload_creates_evidence_and_audit_event(client, identity_fixture):
    admin = identity_fixture["admin"]

    response = client.post(
        "/api/v1/evidence",
        json={
            "title": "Sample Evidence",
            "sha256_hash": "f" * 64,
            "storage_uri": "s3://bucket/evidence.json",
        },
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 201
    payload = response.get_json()
    assert payload["title"] == "Sample Evidence"
    assert payload["organization_id"] == identity_fixture["org_a"].id
    assert payload["sha256_hash"] == "f" * 64

    with client.application.app_context():
        evidence = Evidence.query.get(payload["id"])
        assert evidence is not None
        assert evidence.organization_id == identity_fixture["org_a"].id

        audit_event = AuditEvent.query.filter_by(entity_id=evidence.id, event_type="evidence.uploaded").first()
        assert audit_event is not None
        assert audit_event.actor_id == admin.id


def test_reconciliation_run_requires_permission(client, identity_fixture):
    viewer = identity_fixture["viewer"]

    response = client.post(
        "/api/v1/reconciliation/run",
        json={
            "rule_code": "MISSING_BALANCE",
            "description": "Missing balance evidence detected",
        },
        headers={"Authorization": f"Bearer {make_token(viewer)}"},
    )

    assert response.status_code == 403


def test_reconciliation_run_creates_finding_and_audit_event(client, identity_fixture):
    admin = identity_fixture["admin"]

    response = client.post(
        "/api/v1/reconciliation/run",
        json={
            "rule_code": "MISSING_BALANCE",
            "description": "Missing balance evidence detected",
            "severity": "high",
        },
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 201
    payload = response.get_json()
    assert payload["rule_code"] == "MISSING_BALANCE"
    assert payload["severity"] == "high"
    assert payload["status"] == "new"

    with client.application.app_context():
        finding = ReconciliationFinding.query.get(payload["id"])
        assert finding is not None
        assert finding.organization_id == identity_fixture["org_a"].id

        audit_event = AuditEvent.query.filter_by(entity_id=finding.id, event_type="reconciliation.run").first()
        assert audit_event is not None
        assert audit_event.actor_id == admin.id


def test_reconciliation_findings_are_scoped_to_user_organization(client, identity_fixture):
    admin = identity_fixture["admin"]
    org_b = identity_fixture["org_b"]

    with client.application.app_context():
        finding = ReconciliationFinding(
            organization_id=org_b.id,
            rule_code="CROSS_ORG",
            description="Test cross organization finding",
            severity="low",
            metadata_json={"source": "test"},
        )
        db.session.add(finding)
        db.session.commit()
        finding_id = finding.id

    response = client.get(
        f"/api/v1/reconciliation/findings?organization_id={org_b.id}",
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert any(item["id"] == finding_id for item in payload["findings"])
