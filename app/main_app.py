# from datetime import time
import time

import uvicorn
from fastapi import FastAPI, Header, Request, status
from contextlib import contextmanager, asynccontextmanager
from fastapi.staticfiles import StaticFiles

from app.routes import ( 
    blog_router, 
    user_router, 
    auth_router, 
    item_router 
)

from app.core.middleware import RequestLoggingMiddleware
from app.core.lifespan import lifespan
from app.core.logger import logger
from app.core.config import get_settings
from app.core.instrumentation import instrument_app
from app.middleware.cors import setup_cors

# from app.db.async_db.async_session import init_db
from app.db.session import engine, init_db
from app.db.base import Base


settings = get_settings()

# ======================== APP ======================== #
app = FastAPI(
    lifespan=lifespan,

    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="A Complete Guide on FastAPI",

    # openapi_url=f"{settings.API_V1_STR}/openapi.json",
    # docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
    # redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,
)

# Factory Pattern
# def create_app() -> FastAPI:
#     app = FastAPI(lifespan=lifespan)

#     # register routers here later
#     return app

# app = create_app()


# ======================== OTEL OBSERVABILITY ======================== #
# instrument_app(app)


# ======================== CORS ======================== #
setup_cors(app)


# ======================= LIFESPAN ======================= #
# ------------- on_event -------------
# @app.on_event("startup")
# def startup():
#     logger.info("Application started")
#     # print("App started")

# @app.on_event("shutdown")
# async def shutdown():
#     logger.info("Application stopped")
#     # print("App stopped")

# ------------- asynccontextmanager -------------
# # @asynccontextmanager
# @contextmanager
# async def lifespan(app: FastAPI):
#     logger.log
#     # startup
#     app.state.db = init_db() # connect()
#     print("DB connected")

#     yield

#     # shutdown
#     # app.state.db.close()
#     print("DB closed")


# ======================== STATIC FILES ======================== #

# mount(path, app, name)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
app.mount("/static", StaticFiles(directory="static"), name="static")


# ======================= MIDDLEWARES ======================= #

# app.add_middleware(RequestLoggingMiddleware)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Security headers
# app.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=settings.ALLOWED_HOSTS if hasattr(settings, "ALLOWED_HOSTS") else ["*"]
# )


# ======================= APIs ======================= #

@app.get("/")
async def root():
    return {"message": "Hello World!"}

# @app.get('/get_headers', status_code=status.HTTP_200_OK)
# async def get_headers(
#     accept: str | None = Header(None),
#     content_type: str | None = Header(None),
#     user_agent: str | None = Header(None ),
#     host: str | None = Header(None),
#     authorization: str | None = Header(None),
#     x_request_id: str | None = Header(None),
# ):
#     request_headers = {}

#     request_headers["Accept"] = accept
#     request_headers["Content-Type"] = content_type # Application/Json
#     request_headers["User_Agent"] = user_agent
#     request_headers["Host"] = host
#     request_headers["Authorization"] = authorization
#     request_headers["x_request_id"] = x_request_id

#     return request_headers


# ======================= ROUTES ======================= #

app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)
app.include_router(item_router.router)
# app.include_router(book_router, prefix=f"/api/{version}/books")


# ======================= * ======================= #

# Debugging
if __name__ == '__main__': # Only execute when this file called
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=9000
    )
# python3 main.py

# FastAPI is ASGI (Async Server)
    # Uvicorn
    # Starlette
    # ASGI servers