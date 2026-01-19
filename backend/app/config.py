
Central configuration spine for VERSION DOOM.

This file is
- Read-only at runtime
- Imported exactly once
- The single source of truth for environment-level behavior

NO side effects.
NO IO.
NO dynamic mutation.


from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig
    service_name str
    environment str
    version str
    debug bool
    allowed_origins tuple[str, ...]


def _env(key str, default str) - str
    return os.getenv(key, default)


CONFIG = AppConfig(
    service_name=_env(SERVICE_NAME, sentinel-pv),
    environment=_env(ENVIRONMENT, local),
    version=_env(SERVICE_VERSION, 0.1.0),
    debug=_env(DEBUG, false).lower() == true,
    allowed_origins=tuple(
        o.strip()
        for o in _env(ALLOWED_ORIGINS, ).split(,)
        if o.strip()
    ),
)
