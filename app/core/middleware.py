import time
from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware

from http import HTTPStatus
from app.core.logger import logger

# # Custom:
# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response

class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        # ---- Extract info ----
        client_host = request.client.host
        client_port = request.client.port

        method = request.method
        path = request.url.path
        http_version = request.scope.get("http_version", "1.1")

        status_code = response.status_code
        status_phrase = HTTPStatus(status_code).phrase

        logger.info(
            f'{client_host}:{client_port} - '
            f'"{method} {path} HTTP/{http_version}" '
            f'{status_code} {status_phrase} '
            f'{process_time:.3f}s'
        )

        return response
