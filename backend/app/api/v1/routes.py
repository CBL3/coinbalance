from datetime import datetime, timezone

from flask import current_app, g, jsonify, request

from app.core.audit import AuditEvent
from app.core.auth import require_organization_access, requires_auth, requires_permission
from app.extensions import db
from app.modules.evidence.models import Evidence
from app.modules.reconciliation.models import ReconciliationFinding

from app.api.v1 import api_v1


@api_v1.get("/health")
def health():
    return jsonify(
        {
            "api_version": "v1",
            "environment": current_app.config.get("COINBALANCE_ENV", "development"),
            "phase": "identity-audit-foundation",
            "project": "coinbalance",
            "regulated_activity": False,
            "regulated_activity_enabled": False,
            "regulatory_scope": "non_regulated_operational_intelligence",
            "scope": "technology-platform",
            "service": "coinbalance-api",
            "status": "ok",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "version": current_app.config["COINBALANCE_VERSION"],
        }
    )


@api_v1.get("/identity/me")
@requires_auth
def identity_me():
    return jsonify(g.user.to_dict())


@api_v1.get("/audit/events")
@requires_permission("audit:read")
def audit_events():
    requested_organization_id = request.args.get("organization_id")
    user = g.user

    query = AuditEvent.query.order_by(AuditEvent.created_at.desc())
    if user.is_system_admin():
        if requested_organization_id:
            query = query.filter_by(organization_id=requested_organization_id)
    else:
        if requested_organization_id and requested_organization_id != user.organization_id:
            require_organization_access(requested_organization_id)
        query = query.filter_by(organization_id=user.organization_id)

    events = query.limit(100).all()
    return jsonify({"events": [event.to_dict() for event in events]})


@api_v1.get("/institutional/scope")
def institutional_scope():
    return jsonify(
        {
            "platform": "CoinBalance",
            "positioning": [
                "inteligencia_operacional",
                "governanca_algoritmica",
                "rastreabilidade",
                "reconciliacao_informacional",
                "evidencias",
                "suporte_decisao",
            ],
            "not_characterized_as": [
                "instituicao_financeira",
                "exchange",
                "custodiante",
                "intermediadora_pagamento",
                "instituicao_pagamento",
                "iniciadora_pagamento",
                "entidade_liquidacao",
                "operadora_recursos_terceiros",
            ],
            "regulated_activity_enabled": False,
        }
    )


@api_v1.post("/evidence")
@requires_permission("evidence:upload")
def upload_evidence():
    data = request.get_json(silent=True) or {}
    user = g.user

    if not user.organization_id and not user.is_system_admin():
        return jsonify({"error": "Organização obrigatória para upload de evidências."}), 400

    organization_id = user.organization_id
    if user.is_system_admin():
        organization_id = data.get("organization_id") or user.organization_id
    if not organization_id:
        return jsonify({"error": "organization_id é obrigatório."}), 400

    title = data.get("title")
    sha256_hash = data.get("sha256_hash")
    storage_uri = data.get("storage_uri")
    metadata = data.get("metadata", {})

    if not title or not sha256_hash or not storage_uri:
        return jsonify({"error": "title, sha256_hash e storage_uri são obrigatórios."}), 400

    evidence = Evidence(
        organization_id=organization_id,
        title=title,
        sha256_hash=sha256_hash,
        storage_uri=storage_uri,
        metadata_json=metadata,
    )
    db.session.add(evidence)
    db.session.flush()

    AuditEvent.record_event(
        event_type="evidence.uploaded",
        entity_type="evidence",
        organization_id=organization_id,
        actor_id=user.id,
        entity_id=evidence.id,
        metadata={"title": title, "storage_uri": storage_uri},
    )
    db.session.commit()

    return jsonify(evidence.to_dict()), 201


@api_v1.get("/reconciliation/findings")
@requires_permission("reconciliation:read")
def reconciliation_findings():
    requested_organization_id = request.args.get("organization_id")
    user = g.user

    query = ReconciliationFinding.query.order_by(ReconciliationFinding.created_at.desc())
    if user.is_system_admin():
        if requested_organization_id:
            query = query.filter_by(organization_id=requested_organization_id)
    else:
        if requested_organization_id and requested_organization_id != user.organization_id:
            require_organization_access(requested_organization_id)
        query = query.filter_by(organization_id=user.organization_id)

    findings = query.limit(100).all()
    return jsonify({"findings": [finding.to_dict() for finding in findings]})


@api_v1.post("/reconciliation/run")
@requires_permission("reconciliation:run")
def reconciliation_run():
    data = request.get_json(silent=True) or {}
    user = g.user

    if not user.organization_id and not user.is_system_admin():
        return jsonify({"error": "Organização obrigatória para execução de reconciliação."}), 400

    organization_id = user.organization_id
    if user.is_system_admin():
        organization_id = data.get("organization_id") or user.organization_id
    if not organization_id:
        return jsonify({"error": "organization_id é obrigatório."}), 400

    rule_code = data.get("rule_code")
    description = data.get("description")
    severity = data.get("severity", "medium")
    metadata = data.get("metadata", {})

    if not rule_code or not description:
        return jsonify({"error": "rule_code e description são obrigatórios."}), 400

    finding = ReconciliationFinding(
        organization_id=organization_id,
        rule_code=rule_code,
        severity=severity,
        status="new",
        description=description,
        metadata_json=metadata,
    )
    db.session.add(finding)
    db.session.flush()

    AuditEvent.record_event(
        event_type="reconciliation.run",
        entity_type="reconciliation_finding",
        organization_id=organization_id,
        actor_id=user.id,
        entity_id=finding.id,
        metadata={"rule_code": rule_code, "severity": severity},
    )
    db.session.commit()

    return jsonify(finding.to_dict()), 201
