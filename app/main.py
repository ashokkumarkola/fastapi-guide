from fastapi import FastAPI, Header, status

from app.db.session import engine
from app.db.base import Base

from app.routers.blog_router import router as blog_router
from app.routers.user_router import router as user_router
from app.routers.auth_router import router as auth_router
from app.routers.books_router import router as book_router

from app.core.logger import logger

from contextlib import asynccontextmanager
from app.db.async_db.async_session import init_db

# Import models so SQLAlchemy registers them
# import api.models
from app import models

# @asynccontextmanager
# async def life_sapn(app:FastAPI):
#     print(f"Server is starting...")
#     init_db()
#     yield
#     print(f"Server has been stopped")

version = "v1"
app = FastAPI(
    title="FastAPIGuide",
    description="A Complete Guide on FastAPI",
    version=version
)
# app = FastAPI(title="FastAPI Guide")

# Create tables (dev only)
models.Base.metadata.create_all(bind=engine)
# Base.metadata.create_all(bind=engine)

# @app.on_event("startup")
# def startup():
#     logger.info("Application started")

@app.get("/")
def read_root():
    return {"message": "API running"}

# @app.get("/home", tags=['Root'])
# def read_root():
#     return {"Home": "Welcome to my fastapi application!"}

@app.get('/get_headers', status_code=status.HTTP_200_OK)
async def get_headers(
    accept: str | None = Header(None),
    content_type: str | None = Header(None),
    user_agent: str | None = Header(None ),
    host: str | None = Header(None),
    authorization: str | None = Header(None),
    x_request_id: str | None = Header(None),
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type # Application/Json
    request_headers["User_Agent"] = user_agent
    request_headers["Host"] = host
    request_headers["Authorization"] = authorization
    request_headers["x_request_id"] = x_request_id

    return request_headers

app.include_router(blog_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(book_router, prefix=f"/api/{version}/books")

# Debugging
# if __name__ == '__main__':
#     uvicorn.run(
#         app,
#         host='127.0.0.1',
#         port=9000
#     )
# python3 main.py