# app/core/app.py

import time
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from app.routes import (
    blog_router,
    user_router,
    auth_router,
    item_router,
    purchase_router
)

from app.core.config import get_settings
from app.core.lifespan import lifespan
from app.middleware.cors import setup_cors
# from app.core.instrumentation import instrument_app

settings = get_settings()

def create_app() -> FastAPI:
    """Application factory pattern"""
    app = FastAPI(
        lifespan=lifespan,

        title=settings.PROJECT_NAME,
        description="A Complete Guide on FastAPI",
        # summary="A Complete Guide on FastAPI by Ashoka",
        version=settings.VERSION,
        
        # openapi_url=f"{settings.API_V1_STR}/openapi.json",
        # docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
        # redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,

        # terms_of_service="http://example.com/terms/",
        # contact={
        #     "name": "Deadpoolio the Amazing",
        #     "url": "http://x-force.example.com/contact/",
        #     "email": "dp@x-force.example.com",
        # },
        # license_info={
        #     "name": "Apache 2.0",
        #     "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        # },
    )

    # ================= CORS =================
    setup_cors(app)

    # ================= STATIC FILES =================
    app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # ================= MIDDLEWARE =================
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        start_time = time.perf_counter()
        response = await call_next(request)
        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response

    # ================= ROUTES =================
    register_routes(app)

    # ================= OBSERVABILITY =================
    # instrument_app(app)

    return app


def register_routes(app: FastAPI):
    app.include_router(blog_router.router)
    app.include_router(user_router.router)
    app.include_router(auth_router.router)
    app.include_router(item_router.router)
    app.include_router(purchase_router.router)

    # @app.get("/")
    # async def root():
    #     return {"message": "Hello World!"}
    
    @app.get("/")
    async def root():
        return {
            "message": f"Welcome to {settings.PROJECT_NAME}",
            "version": settings.VERSION,
            "docs": "/docs",
            "environment": settings.ENVIRONMENT
        }
    
    @app.get("/health")
    async def health_check():
        return {"status": "healthy"}