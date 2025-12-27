from fastapi import APIRouter
from app.models import Log

router = APIRouter( 
    prefix="/logs",
    tags=["Logs"]
    )

logs_db = []

@router.post("/logs")
def ingest_log(log : Log):
    logs_db.append(log)
    return {
        "status": "success",
        "message": "Log received",
        "log": log
    }

