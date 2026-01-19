import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import logging


logger = logging.getLogger("request")


class RequestContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))

        request.state.request_id = request_id

        logger.info(
            "incoming_request",
            extra={"request_id": request_id},
        )

        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id

        logger.info(
            "completed_request",
            extra={"request_id": request_id},
        )

        return response
