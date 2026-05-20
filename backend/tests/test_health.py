from app import create_app


def test_health_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["service"] == "coinbalance-api"
    assert payload["status"] == "ok"
    assert payload["version"] == "0.1.0-alpha"
    assert payload["api_version"] == "v1"
    assert payload["project"] == "coinbalance"
    assert payload["regulated_activity"] is False
    assert payload["regulated_activity_enabled"] is False
    assert payload["regulatory_scope"] == "non_regulated_operational_intelligence"


def test_institutional_scope_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/v1/institutional/scope")

    assert response.status_code == 200
    payload = response.get_json()
    assert payload["platform"] == "CoinBalance"
    assert payload["regulated_activity_enabled"] is False
    assert "reconciliacao_informacional" in payload["positioning"]
    assert "exchange" in payload["not_characterized_as"]
