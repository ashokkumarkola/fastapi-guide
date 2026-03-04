from datetime import time

from fastapi import FastAPI, Header, Request, status
from contextlib import contextmanager, asynccontextmanager
from fastapi.staticfiles import StaticFiles

from app.db.session import engine, init_db
from app.db.base import Base

from app.routes.blog_router import router as blog_router
from app.routes.user_router import router as user_router
from app.routes.auth_router import router as auth_router
from app.routes.item_router import router as item_router
# from app.routers.books_router import router as book_router

# from app.routes import ( 
#     blog_router, 
#     user_router, 
#     auth_router, 
#     item_router 
# )

from app.core.middleware import RequestLoggingMiddleware
from app.core.lifespan import lifespan
from app.core.logger import logger
from app.core.config import get_settings
from app.middleware.cors import setup_cors

# from contextlib import asynccontextmanager
# from app.db.async_db.async_session import init_db

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

# def create_app() -> FastAPI:
#     app = FastAPI(lifespan=lifespan)

#     # register routers here later
#     return app

# app = create_app()

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

# ======================= MIDDLEWARES ======================= #
# app.add_middleware(RequestLoggingMiddleware)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# ======================= APIs ======================= #
@app.get("/")
async def root():
    return {"message": "Hello World!"}

# @app.get("/home", tags=['Root'])
# def read_root():
#     return {"Home": "Welcome to my fastapi application!"}

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
app.include_router(blog_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(item_router)
# app.include_router(book_router, prefix=f"/api/{version}/books")

# ======================= * ======================= #
# def create_application() -> FastAPI:
#     """Application factory pattern"""
#     application = FastAPI(
#         title=settings.PROJECT_NAME,
#         version=settings.VERSION,
#         openapi_url=f"{settings.API_V1_STR}/openapi.json",
#         docs_url="/docs" if settings.ENVIRONMENT == "development" else None,
#         redoc_url="/redoc" if settings.ENVIRONMENT == "development" else None,
#     )
    
#     # Set up CORS
#     application.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"] if settings.ENVIRONMENT == "development" else ["your-production-domain.com"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )
    
#     # Add security headers
#     application.add_middleware(
#         TrustedHostMiddleware,
#         allowed_hosts=["*"] if settings.ENVIRONMENT == "development" else ["your-domain.com"]
#     )
    
#     # Include routers
#     application.include_router(auth.router, prefix=settings.API_V1_STR)
#     application.include_router(items.router, prefix=settings.API_V1_STR)
    
#     @application.get("/")
#     async def root():
#         return {
#             "message": f"Welcome to {settings.PROJECT_NAME}",
#             "version": settings.VERSION,
#             "docs": "/docs",
#             "environment": settings.ENVIRONMENT
#         }
    
#     @application.get("/health")
#     async def health_check():
#         return {"status": "healthy"}
    
#     return application

# app = create_application()

# Debugging
# if __name__ == '__main__': # Only execute when this file called
#     uvicorn.run(
#         app,
#         host='127.0.0.1',
#         port=9000
#     )
# python3 main.py

# FastAPI is ASGI (Async Server)
    # Uvicorn
    # Starlette
    # ASGI servers