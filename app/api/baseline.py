from fastapi import APIRouter, Depends
from app.dependencies import get_db
from app.api.metrics import get_metrics
from app.Anomaly.anomaly_engine import detect_anomalies
from app.Baseline.baseline_model import Baseline
from app.Alert.alert_engine import apply_alert_rules
from app.Alert.default_rules import DEFAULT_RULES


router = APIRouter()

BASELINE: Baseline | None = None

@router.post("/baseline/set")
def set_baseline(baseline: Baseline):
    global BASELINE 
    BASELINE = baseline
    return {"status": "baseline set"}

@router.get("/baseline/check")
def check_baseline(db=Depends(get_db)):
    if BASELINE is None:
        return {"error": "Baseline not set"}

    current_metrics = get_metrics(db)
    anomalies = detect_anomalies(current_metrics, BASELINE)

    alerts = apply_alert_rules(anomalies, DEFAULT_RULES)
    
    return {
        "alerts": alerts,
        "anomalies": anomalies,
        "current_metrics": {
            "error_rate": current_metrics["error_rate"],
            "logs_per_minute": current_metrics["logs_per_minute"]
        }
    }

