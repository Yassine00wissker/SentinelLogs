from datetime import datetime
from app.Anomaly.anomaly_model import Anomaly
from app.Anomaly.severity import calculate_severity

def detect_anomalies(metrics: dict, baseline):
    anomalies = []

    # --- LOG VOLUME ---
    values = metrics["logs_per_minute"].values()
    if values:
        current_avg = sum(values) / len(values)
        threshold = baseline.avg_logs_per_min * 2

        if current_avg > threshold:
            anomalies.append(
                Anomaly(
                    type="LOG_VOLUME_SPIKE",
                    severity=calculate_severity(current_avg, threshold),
                    value=current_avg,
                    threshold=threshold,
                    timestamp=datetime.utcnow()
                )
            )

    # --- ERROR RATE ---
    error_rate = metrics["error_rate"]
    threshold = baseline.avg_error_rate + 5

    if error_rate > threshold:
        anomalies.append(
            Anomaly(
                type="ERROR_RATE_SPIKE",
                severity=calculate_severity(error_rate, threshold),
                value=error_rate,
                threshold=threshold,
                timestamp=datetime.utcnow()
            )
        )

    return anomalies
