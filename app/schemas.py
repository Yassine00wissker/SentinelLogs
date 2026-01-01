from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal, Optional

class LogCreate(BaseModel):
    service: str = Field(..., example="auth-service")
    level: Literal["INFO", "WARNING", "ERROR"]
    message: str
    timestamp: Optional[datetime] = None
