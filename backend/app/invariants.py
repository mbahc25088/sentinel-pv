"""
Hard runtime invariants for VERSION DOOM.
Any violation MUST crash the service immediately.
"""

import os
from typing import List


class InvariantViolation(RuntimeError):
    pass


def _require_env(var: str) -> str:
    value = os.getenv(var)
    if not value:
        raise InvariantViolation(f"Missing required environment variable: {var}")
    return value


def _require_one_of(vars: List[str]) -> str:
    for v in vars:
        if os.getenv(v):
            return v
    raise InvariantViolation(
        f"One of the following environment variables must be set: {vars}"
    )


def assert_runtime_invariants() -> None:
    """
    Executed during startup.
    Any failure aborts process.
    """

    _require_env("APP_ENV")
    _require_env("APP_NAME")

    if os.getenv("APP_ENV") not in {"local", "dev", "staging", "prod"}:
        raise InvariantViolation(
            f"Invalid APP_ENV value: {os.getenv('APP_ENV')}"
        )

    # Exactly one DB mode allowed
    _require_one_of(
        [
            "DATABASE_URL",
            "POSTGRES_HOST",
        ]
    )
