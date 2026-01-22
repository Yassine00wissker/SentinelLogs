from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.api.metrics import get_metrics
from app.Anomaly.anomaly_engine import detect_anomalies
from app.Alert.alert_engine import apply_alert_rules
from app.Alert.alert_rule_model import AlertRule
from app.Baseline.baseline_model import Baseline

router = APIRouter()

# TEMP (later move to DB)
BASELINE = Baseline(
    service="global",
    avg_logs_per_min=2,
    avg_error_rate=0.15,
    normal_hours=list(range(0, 24))
)

RULES = [
    AlertRule(
        anomaly_type="ERROR_RATE_SPIKE",
        min_severity="MEDIUM",
        cooldown_minutes=10
    )
]

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    metrics = get_metrics(db)
    anomalies = detect_anomalies(metrics, BASELINE)
    alerts = apply_alert_rules(anomalies, RULES)

    return {
        "metrics": metrics,
        "anomalies": [a.dict() for a in anomalies],
        "alerts": [a.dict() for a in alerts]
    }

@router.get("/dashboard/summary")
def summary(db: Session = Depends(get_db)):
    metrics = get_metrics(db)
    anomalies = detect_anomalies(metrics, BASELINE)
    alerts = apply_alert_rules(anomalies, RULES)

    status = "OK"

    if any(a.severity == "CRITICAL" for a in alerts):
        status = "CRITICAL"
    elif any(a.severity in ("HIGH","MEDIUM") for a in alerts):
        status = "WARNING"

    return {
        "status":status,
        "total_logs": metrics["total_logs"],
        "error_rate": metrics["error_rate"],
        "active_alerts": len(alerts),
        "anomalies_detected": len(anomalies),
        "timestamp": metrics.get("timestamp")
    }
