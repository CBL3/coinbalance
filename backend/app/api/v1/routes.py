from datetime import datetime, timezone

from flask import current_app, jsonify

from app.api.v1 import api_v1


@api_v1.get("/health")
def health():
    return jsonify(
        {
            "api_version": "v1",
            "environment": current_app.config.get("COINBALANCE_ENV", "development"),
            "phase": "foundation",
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
