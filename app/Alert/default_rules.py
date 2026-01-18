from app.Alert.alert_rule_model import AlertRule

DEFAULT_RULES = [
    AlertRule(
        anomaly_type="LOG_VOLUME_SPIKE",
        min_severity="HIGH",
        cooldown_minutes=5
    ),
    AlertRule(
        anomaly_type="ERROR_RATE_SPIKE",
        min_severity="MEDIUM",
        cooldown_minutes=10
    )
]
