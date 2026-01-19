"""
Lifecycle spine — authoritative runtime state machine.
LOCKED NAME. DO NOT RENAME.
"""

from enum import Enum
from typing import Optional

from app.invariants import assert_runtime_invariants


class LifecycleState(str, Enum):
    INIT = "INIT"
    RUNNING = "RUNNING"
    SHUTTING_DOWN = "SHUTTING_DOWN"


_state: LifecycleState = LifecycleState.INIT
_startup_complete: bool = False


async def startup_event() -> None:
    global _state, _startup_complete

    assert_runtime_invariants()

    _state = LifecycleState.RUNNING
    _startup_complete = True


async def shutdown_event() -> None:
    global _state
    _state = LifecycleState.SHUTTING_DOWN


def get_lifecycle_state() -> dict:
    return {
        "state": _state,
        "startup_complete": _startup_complete,
    }
