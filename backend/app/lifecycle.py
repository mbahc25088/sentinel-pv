from app.invariants import assert_runtime_invariants
from app.db import init_engine, shutdown_engine


async def startup_event() -> None:
    assert_runtime_invariants()
    init_engine()


async def shutdown_event() -> None:
    shutdown_engine()
