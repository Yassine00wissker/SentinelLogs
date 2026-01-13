from fastapi import APIRouter, Depends
from app.dependencies import get_db
from app.models import Log
from sqlalchemy.orm import Session
from collections import Counter

router = APIRouter()

def total_logs(db: Session):
    return db.query(Log).count()

def logs_by_level(db: Session):
    logs =  db.query(Log.level).all()
    return dict(Counter(log.level for log in logs))

def logs_by_service(db: Session):
    logs =  db.query(Log.service).all()
    return dict(Counter(log.service for log in logs))

def error_rate(db:Session):
    total = db.query(Log).count()
    if total == 0:
        return 0
    errors = db.query(Log).filter(Log.level == "ERROR").count()
    return errors / total

def logs_per_minute(db:Session):
    logs = db.query(Log.timestamp).all()
    result = {}

    for log in logs:
        minute = log.timestamp.strftime("%Y-%m-%d %H:%M")
        result[minute] = result.get(minute, 0) + 1
    
    return result

@router.get("/metrics")
def get_metrics(db:Session = Depends(get_db)):
    return {
        "total_logs": total_logs(db),
        "logs_by_level": logs_by_level(db),
        "logs_by_service": logs_by_service(db),
        "error_rate": error_rate(db),
        "logs_per_minute": logs_per_minute(db)
    }