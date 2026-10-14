from fastapi import FastAPI

from app.v1.config.settings import settings
from app.v1.routers.agent import router as agent_router
from app.v1.routers.health import router as health_router


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
)

app.include_router(health_router, prefix="/api/v1")
app.include_router(agent_router, prefix="/api/v1")


@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "api_version": "v1",
        "status": "running",
    }