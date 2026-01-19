from fastapi import FastAPI
from app.lifecycle import get_lifecycle_state
from app.config import CONFIG


app = FastAPI(
    title=CONFIG.service_name,
    debug=CONFIG.debug,
)


@app.get("/health", tags=["system"])
def health():
    return {
        "status": "ok",
        "service": CONFIG.service_name,
        "version": CONFIG.version,
        "environment": CONFIG.environment,
        "lifecycle": get_lifecycle_state(),
    }


@app.get("/config", tags=["system"])
def config_snapshot():
    """
    Read-only configuration snapshot.
    Safe for diagnostics.
    """
    return {
        "service_name": CONFIG.service_name,
        "environment": CONFIG.environment,
        "version": CONFIG.version,
        "debug": CONFIG.debug,
        "allowed_origins": CONFIG.allowed_origins,
    }
