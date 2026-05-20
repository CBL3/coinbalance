import pytest
from app import create_app
from app.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


@pytest.fixture
def app():
    app = create_app(TestConfig)
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_hardware_interface_success(client):
    """
    Testa se o HAL aceita um payload genérico bem-formado.
    """
    payload = {
        "hardware_id": "XYRON-001",
        "event_type": "NFC_READ",
        "payload": {
            "tag_id": "04:XX:YY:ZZ",
            "timestamp": "2026-05-20T10:00:00Z"
        }
    }
    
    response = client.post("/api/v1/hardware/interface", json=payload)
    
    assert response.status_code == 202
    data = response.get_json()
    assert data["status"] == "accepted"
    assert "XYRON-001" in data["message"]
    assert data["processed_payload"]["tag_id"] == "04:XX:YY:ZZ"


def test_hardware_interface_missing_data(client):
    """
    Testa se o HAL rejeita payloads mal-formados.
    """
    # Missing event_type
    payload = {
        "hardware_id": "XYRON-001",
        "payload": {}
    }
    
    response = client.post("/api/v1/hardware/interface", json=payload)
    
    assert response.status_code == 400
    
    # Empty payload
    response = client.post("/api/v1/hardware/interface", json={})
    assert response.status_code == 400
