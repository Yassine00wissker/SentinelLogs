from sqlalchemy.orm import Session
from app.models import Log
from datetime import datetime

def query_logs (db:Session,
                level: str | None = None,
                service: str | None = None,
                keyword: str | None = None,
                start: datetime | None = None,
                end: datetime | None = None,):
    query = db.query(Log)

    if level:
        query = query.filter(Log.level == level)

    if service:
        query = query.filter(Log.service == service)

    if keyword:
        query = query.filter(Log.message.ilike(f"%{keyword}%"))

    if start and end:
        query = query.filter(Log.timestamp.between(start, end))

    return query.all()
