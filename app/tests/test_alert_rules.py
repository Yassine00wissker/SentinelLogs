from datetime import datetime, timedelta
from app.Anomaly.anomaly_model import Anomaly
from app.Alert.alert_engine import apply_alert_rules
from app.Alert.alert_rule_model import AlertRule
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_alert_triggered():
    anomaly = Anomaly(
        type="ERROR_RATE_SPIKE",
        severity="HIGH",
        value=10,
        threshold=5,
        timestamp=datetime.utcnow()
    )

    rule = AlertRule(
        anomaly_type="ERROR_RATE_SPIKE",
        min_severity="MEDIUM",
        cooldown_minutes=10
    )

    alerts = apply_alert_rules([anomaly], [rule])
    assert len(alerts) == 1

def test_alert_blocked_by_cooldown():
    anomaly = Anomaly(
        type="ERROR_RATE_SPIKE",
        severity="HIGH",
        value=10,
        threshold=5,
        timestamp=datetime.utcnow()
    )

    rule = AlertRule(
        anomaly_type="ERROR_RATE_SPIKE",
        min_severity="LOW",
        cooldown_minutes=10
    )

    apply_alert_rules([anomaly], [rule])
    alerts = apply_alert_rules([anomaly], [rule])

    assert len(alerts) == 0

def test_alerts_exist_after_baseline_set():
    baseline_payload = {
        "service": "global",
        "avg_logs_per_min": 5,
        "avg_error_rate": 0.01,
        "normal_hours": [8, 9, 10, 11, 12, 13, 14, 15]
    }
    res = client.post("/baseline/set", json=baseline_payload)
    assert res.status_code == 200

    response = client.get("/baseline/check")
    assert response.status_code == 200

    data = response.json()
    assert "alerts" in data
    assert "anomalies" in data

