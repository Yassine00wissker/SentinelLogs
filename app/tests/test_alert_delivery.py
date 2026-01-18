from app.Alert.alert_delivery import deliver_alert
from app.Anomaly.anomaly_model import Anomaly
from datetime import datetime

def test_console_delivery(capsys):
    alert = Anomaly(
        type="ERROR_RATE_SPIKE",
        severity="HIGH",
        value=10,
        threshold=5,
        timestamp=datetime.utcnow()
    )

    deliver_alert(alert, channel="console")

    captured = capsys.readouterr()
    assert "ERROR_RATE_SPIKE" in captured.out
    assert "HIGH" in captured.out
