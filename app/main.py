from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.logs import router as logs_router
from app.database import engine
from app.models import Base
from app.api.metrics import router as metrics_router
from app.api.baseline import router as baseline_router
from app.api.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="SENTINELLOGS")

app.include_router(health_router)
app.include_router(logs_router)
app.include_router(metrics_router)
app.include_router(baseline_router)
app.include_router(dashboard_router)