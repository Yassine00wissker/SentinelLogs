from fastapi import APIRouter, Depends
from app.dependencies import get_db
from app.models import Log
from sqlalchemy.orm import Session
import pandas as pd

router = APIRouter()

def get_logs_df(db:Session) -> pd.DataFrame:
    logs = db.query(Log.timestamp, Log.level, Log.service).all()

    if not logs:
        return pd.DataFrame(columns=["timestamp","level","service"])
    
    df = pd.DataFrame(logs, columns=["timestamp","level","service"])
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

@router.get("/metrics")
def get_metrics(db:Session = Depends(get_db)):
    df = get_logs_df(db)

    total_logs = len(df)

    logs_by_level = (
        df["level"].value_counts().to_dict()
    )

    logs_by_service = (
        df["service"].value_counts().to_dict()
    )

    error_rate = (
        df["level"].eq("ERROR").mean()
        if total_logs > 0 else 0
    )

    logs_per_minute = (
        df.set_index("timestamp")
        .resample("1min")
        .size()
        .rename(lambda x: x.strftime("%Y-%m-%d %H:%M"))
        .to_dict()
    )

    return {
        "total_logs": total_logs,
        "logs_by_level": logs_by_level,
        "logs_by_service": logs_by_service,
        "error_rate": error_rate,
        "logs_per_minute": logs_per_minute
    }