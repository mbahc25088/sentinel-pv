from fastapi import FastAPI

from app.lifecycle import (
    startup_event,
    shutdown_event,
    get_lifecycle_state,
)
from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
)


@app.on_event("startup")
async def _startup():
    await startup_event()


@app.on_event("shutdown")
async def _shutdown():
    await shutdown_event()


@app.get("/")
def root():
    return {
        "service": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "lifecycle": get_lifecycle_state(),
    }
