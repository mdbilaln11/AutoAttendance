from fastapi import FastAPI
from app.api.routes import attendance, health
from app.core.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(health.router)
app.include_router(attendance.router, prefix="/api/v1")
