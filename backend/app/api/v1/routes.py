from datetime import datetime, timezone

from flask import current_app, g, jsonify, request

from app.core.audit import AuditEvent
from app.core.auth import require_organization_access, requires_auth, requires_permission

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
                "intermediadora_financeira",
                "instituicao_pagamento",
                "iniciadora_pagamento",
                "entidade_liquidacao",
                "operadora_recursos_terceiros",
            ],
            "regulated_activity_enabled": False,
        }
    )
