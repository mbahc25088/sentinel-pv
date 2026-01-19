import os


class InvariantViolation(RuntimeError):
    pass


def _require_env(var: str) -> None:
    if not os.getenv(var):
        raise InvariantViolation(f"Missing required environment variable: {var}")


def _require_one_of(vars: list[str]) -> None:
    for v in vars:
        if os.getenv(v):
            return
    raise InvariantViolation(
        f"One of the following environment variables must be set: {vars}"
    )


def assert_runtime_invariants() -> None:
    _require_env("APP_NAME")
    _require_env("APP_ENV")
    _require_one_of(["DATABASE_URL"])
