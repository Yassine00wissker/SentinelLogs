from pydantic import BaseModel, Field
from datetime import datetime 
from typing import Literal

class Log(BaseModel):
    service: str = Field(..., example="auth-server")
    level: Literal["INFO","WARNING","ERROR"]
    message: str
    timestamp: datetime 