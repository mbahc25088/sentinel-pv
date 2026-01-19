from fastapi import FastAPI
from app.lifecycle import (
    LifecycleState,
    get_lifecycle_state,
)

app = FastAPI(title="Sentinel-PV", version="VERSION_DOOM")

@app.get("/health")
def health():
    state = get_lifecycle_state()
    return {
        "status": "ok",
        "phase": state.value,
    }
