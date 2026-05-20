from datetime import datetime, timedelta, timezone

import jwt

from app.core.audit import AuditEvent
from app.extensions import db
from app.modules.identity.models import Role, User
from app.modules.organizations.models import Organization
from app.modules.reconciliation.models import ReconciliationFinding, ReconciliationRule, ReconciliationRun
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


def test_reconciliation_rule_creation_requires_permission(client, identity_fixture):
    viewer = identity_fixture["viewer"]

    response = client.post(
        "/api/v1/reconciliation/rules",
        json={
            "code": "BALANCE_CHECK",
            "name": "Balance check",
            "description": "Verifica divergências de saldo.",
        },
        headers={"Authorization": f"Bearer {make_token(viewer)}"},
    )

    assert response.status_code == 403


def test_reconciliation_rule_creation_and_listing(client, identity_fixture):
    admin = identity_fixture["admin"]
    auditor = identity_fixture["auditor"]

    response = client.post(
        "/api/v1/reconciliation/rules",
        json={
            "code": "BALANCE_CHECK",
            "name": "Balance check",
            "description": "Find divergências de reconciliação.",
            "severity_default": "high",
        },
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 201
    payload = response.get_json()
    assert payload["code"] == "BALANCE_CHECK"
    assert payload["severity_default"] == "high"

    response = client.get(
        "/api/v1/reconciliation/rules",
        headers={"Authorization": f"Bearer {make_token(auditor)}"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert any(rule["code"] == "BALANCE_CHECK" for rule in payload["rules"])


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


def test_reconciliation_run_rejects_missing_rule(client, identity_fixture):
    admin = identity_fixture["admin"]

    response = client.post(
        "/api/v1/reconciliation/run",
        json={
            "rule_code": "UNKNOWN_RULE",
            "description": "Missing rule test",
            "severity": "high",
        },
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 404


def test_reconciliation_run_creates_run_and_finding(client, identity_fixture):
    admin = identity_fixture["admin"]
    org_a = identity_fixture["org_a"]

    with client.application.app_context():
        rule = ReconciliationRule(
            organization_id=org_a.id,
            code="BALANCE_CHECK",
            name="Balance check",
            description="Rule placeholder for run test",
            severity_default="medium",
            metadata_json={"source": "test"},
        )
        db.session.add(rule)
        db.session.commit()
        rule_id = rule.id

    response = client.post(
        "/api/v1/reconciliation/run",
        json={
            "rule_code": "BALANCE_CHECK",
            "description": "Missing balance evidence detected",
            "severity": "high",
            "result_summary": "Saldo divergente detectado",
        },
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 201
    payload = response.get_json()
    assert payload["run"]["status"] == "completed"
    assert payload["finding"]["rule_code"] == "BALANCE_CHECK"

    with client.application.app_context():
        finding = ReconciliationFinding.query.get(payload["finding"]["id"])
        assert finding is not None
        assert finding.organization_id == org_a.id

        run = ReconciliationRun.query.get(payload["run"]["id"])
        assert run is not None
        assert run.rule_id == rule_id

        audit_event = AuditEvent.query.filter_by(entity_id=run.id, event_type="reconciliation.run").first()
        assert audit_event is not None
        assert audit_event.actor_id == admin.id


def test_reconciliation_runs_are_scoped_to_user_organization(client, identity_fixture):
    admin = identity_fixture["admin"]
    org_b = identity_fixture["org_b"]

    with client.application.app_context():
        rule = ReconciliationRule(
            organization_id=org_b.id,
            code="CROSS_ORG",
            name="Cross org rule",
            description="Test rule for cross org run",
            severity_default="low",
            metadata_json={"source": "test"},
        )
        db.session.add(rule)
        db.session.flush()

        run = ReconciliationRun(
            organization_id=org_b.id,
            rule_id=rule.id,
            actor_id=admin.id,
            status="completed",
            result_summary="Cross-org run",
            metadata_json={"source": "test"},
        )
        db.session.add(run)
        db.session.commit()
        run_id = run.id

    response = client.get(
        f"/api/v1/reconciliation/runs?organization_id={org_b.id}",
        headers={"Authorization": f"Bearer {make_token(admin)}"},
    )

    assert response.status_code == 200
    payload = response.get_json()
    assert any(item["id"] == run_id for item in payload["runs"])
