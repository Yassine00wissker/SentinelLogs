from pydantic import BaseModel
from typing import List

class Baseline(BaseModel):
    service : str
    avg_logs_per_min: float
    avg_error_rate: float
    normal_hours: List[int]