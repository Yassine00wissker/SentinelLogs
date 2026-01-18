from app.Alert.alert_rule_model import AlertRule
import requests
def deliver_alert(alert: AlertRule, channel: str = "console"):
    if channel == "console" :
        print_alert(alert)
    elif channel == "webhook":
        send_webhook(alert)
    else:
        raise ValueError("Unsupported alert channel")
    
def print_alert(alert: AlertRule):
    print(
        f"[ALERT] {alert.severity} | {alert.type} | "
        f"value={alert.value} threshold={alert.threshold}"
    )

def send_webhook(alert: AlertRule):
    webhook_url = "http://localhost:9000/alerts"

    payload = {
        "type": alert.type,
        "severity": alert.severity,
        "value": alert.value,
        "threshold": alert.threshold,
        "timestamp": alert.timestamp.isoformat()
    }

    try:
        requests.post(webhook_url, json=payload, timeout=2)
    except Exception as e:
        print("Webhook delivery failed:", e)
