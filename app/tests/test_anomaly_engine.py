from datetime import datetime
from app.Anomaly.anomaly_engine import detect_anomalies
from app.Baseline.baseline_model import Baseline

def test_log_volume_anomaly():
    metrics = {
        "logs_per_minute": {"2026-01-01 10:00": 50},
        "error_rate": 0.1
    }

    baseline = Baseline(
        service="global",
        avg_logs_per_min=5,
        avg_error_rate=0.01,
        normal_hours=[9, 10, 11]
    )

    anomalies = detect_anomalies(metrics, baseline)

    assert len(anomalies) == 1
    assert anomalies[0].type == "LOG_VOLUME_SPIKE"
    assert anomalies[0].severity in ["HIGH", "CRITICAL"]
