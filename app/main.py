from fastapi import FastAPI, Header, status
from contextlib import contextmanager, asynccontextmanager

from app.db.session import engine, init_db
from app.db.base import Base

from app.routers.blog_router import router as blog_router
from app.routers.user_router import router as user_router
# from app.routers.auth_router import router as auth_router
# from app.routers.books_router import router as book_router

from app.core.middleware import RequestLoggingMiddleware
from app.core.lifespan import lifespan
from app.core.logger import logger

# from contextlib import asynccontextmanager
# from app.db.async_db.async_session import init_db

# Import models so SQLAlchemy registers them
# import api.models
from app import models


# ======================== APP ======================== #
version = "v1"
app = FastAPI(
    lifespan=lifespan,

    title="FastAPIGuide",
    description="A Complete Guide on FastAPI",
    version=version
)

# def create_app() -> FastAPI:
#     app = FastAPI(lifespan=lifespan)

#     # register routers here later
#     return app


# app = create_app()

# Create tables (dev only)
# models.Base.metadata.create_all(bind=engine)
# Base.metadata.create_all(bind=engine)

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
@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    app.state.db = init_db() # connect()
    print("DB connected")

    yield

    # shutdown
    # app.state.db.close()
    print("DB closed")


# ======================= MIDDLEWARES ======================= #
app.add_middleware(RequestLoggingMiddleware)

# ======================= APIs ======================= #
@app.get("/")
def read_root():
    return {"message": "API running"}

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
# app.include_router(auth_router)
# app.include_router(book_router, prefix=f"/api/{version}/books")

# Debugging
# if __name__ == '__main__':
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