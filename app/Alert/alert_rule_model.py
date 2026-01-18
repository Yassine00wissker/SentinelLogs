from pydantic import BaseModel
from typing import Optional

class AlertRule(BaseModel):
    anomaly_type: str
    min_severity: str
    cooldown_minutes: int
    enabled: bool = True
