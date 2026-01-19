from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from app.config import get_settings

_ENGINE: Engine | None = None
_SessionLocal: sessionmaker | None = None


def init_engine() -> None:
    global _ENGINE, _SessionLocal
    settings = get_settings()

    _ENGINE = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        future=True,
    )
    _SessionLocal = sessionmaker(
        bind=_ENGINE,
        autoflush=False,
        autocommit=False,
        future=True,
    )


def shutdown_engine() -> None:
    global _ENGINE
    if _ENGINE:
        _ENGINE.dispose()
        _ENGINE = None


def get_session():
    if _SessionLocal is None:
        raise RuntimeError("Database engine not initialized")
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
