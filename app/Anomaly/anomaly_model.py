from pydantic import BaseModel
from datetime import datetime

class Anomaly(BaseModel):
    type: str
    severity: str
    value: float
    threshold: float
    timestamp: datetime