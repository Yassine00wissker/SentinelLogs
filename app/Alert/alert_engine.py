from datetime import datetime, timedelta
from app.Alert.severity_order import severity_allowed
from app.Alert.alert_delivery import deliver_alert
LAST_ALERT = {}

def apply_alert_rules(anomalies, rules):
    alerts = []
    now = datetime.utcnow()

    for anomaly in anomalies:
        for rule in rules:
            if not rule.enabled :
                continue

            if anomaly.type != rule.anomaly_type :
                continue

            if not severity_allowed(anomaly.severity, rule.min_severity) :
                continue

            key = (anomaly.type)
            last_time = LAST_ALERT.get(key)

            if last_time:
                if now - last_time < timedelta(minutes=rule.cooldown_minutes):
                    continue
            alert = anomaly
            
            LAST_ALERT[key] = now
            alerts.append(anomaly)

            deliver_alert(alert, channel="console")
    return alerts