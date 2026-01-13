from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_get_logs():
    response = client.get("/logs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_log():
    payload = {
        "service": "auth-service",
        "level": "info",
        "message": "Test log"
    }

    response = client.post("/logs/", json=payload)

    assert response.status_code == 201
    assert response.json()["service"] == "auth-service"


def test_get_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    
def test_get_metrics_content():
    data = client.get("/metrics").json()
    assert "total_logs" in data
    assert "error_rate" in data
