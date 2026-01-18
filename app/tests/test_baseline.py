from fastapi.testclient import TestClient
from app.main import app
from app.api import baseline
client = TestClient(app)

def test_check_baseline_without_setting():
    baseline.BASELINE = None # reset global state
    response = client.get("/baseline/check")

    assert response.status_code == 200
    assert response.json()["error"] == "Baseline not set"

def test_set_baseline():
    payload = {
        "service": "global",
        "avg_logs_per_min": 5,
        "avg_error_rate": 0.05,
        "normal_hours": [8,9,10,11,12,13,14,15,16,17]
    }

    response = client.post("/baseline/set", json=payload)

    assert response.status_code == 200
    assert response.json()["status"] == "baseline set"

def test_check_baseline_after_setting():
    response = client.get("/baseline/check")

    assert response.status_code == 200
    data = response.json()

    assert "anomalies" in data
    assert "current_metrics" in data
    assert "error_rate" in data["current_metrics"]
    assert "logs_per_minute" in data["current_metrics"]