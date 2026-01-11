from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Literal, Optional

class LogCreate(BaseModel):
    service: str = Field(..., example="auth-service")
    level: str = Field(..., example="info")
    message: str
    timestamp: Optional[datetime] = None

    @validator("level", pre=True)
    def normalize_level(cle,v):
        level_map = {
            "info": "INFO",
            "information": "INFO",
            "warn": "WARNING",
            "warning": "WARNING",
            "err": "ERROR",
            "error": "ERROR",
            "critical": "ERROR"
        }
        return level_map.get(str(v).lower(), "INFO")

    @validator("timestamp", pre=True, always=True)
    def set_timestamp(cle, v):
        return v or datetime.utcnow()

class LogResponse(BaseModel):
    id: int
    service: str
    level: str
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True

class LogQuery(BaseModel):
    level: Optional[str] = None
    service: Optional[str] = None
    keyword: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None