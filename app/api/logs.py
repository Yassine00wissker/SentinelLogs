from fastapi import APIRouter, Depends
from app.models import Log
from app.dependencies import get_db
from sqlalchemy.orm import Session
from app.schemas import LogResponse,LogCreate,LogQuery
from app.services.log_service import query_logs

router = APIRouter( 
    prefix="/logs",
    tags=["Logs"]
    )


@router.post("/")
def ingest_log(log : LogCreate, db: Session = Depends(get_db)):
    db_log  = Log(
        service=log.service,
        level=log.level,
        message=log.message,
        timestamp=log.timestamp
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {
        "status": "saved",
        "message": "Log is saved successfuly",
        "log": db_log .id
    }

@router.get("/", response_model=list[LogResponse])
def get_log(query: LogQuery = Depends(),
    db: Session = Depends(get_db)):
    return query_logs(db, level=query.level, service=query.service, keyword=query.keyword, start=query.start, end=query.end)
