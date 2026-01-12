from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Literal, Optional

class LogCreate(BaseModel):
    service: str = Field(..., json_schema_extra={"example":"auth-service"})
    level: str = Field(..., json_schema_extra={"example":"info"})
    message: str
    timestamp: Optional[datetime] = None

    @field_validator("level", mode="before")
    @classmethod
    def normalize_level(cls,v):
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

    @field_validator("timestamp", mode="before")
    @classmethod
    def set_timestamp(cls, v):
        return v or datetime.utcnow()

class LogResponse(BaseModel):
    id: int
    service: str
    level: str
    message: str
    timestamp: datetime

    model_config = {"from_attributes":True}

class LogQuery(BaseModel):
    level: Optional[str] = None
    service: Optional[str] = None
    keyword: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None