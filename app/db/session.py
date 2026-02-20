from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
# from typing import Generator
# from sqlalchemy.ext.asyncio import create_engine, session # create_async_engine, AsyncSession

from app.db.base import Base
from app.core.logger import logger

# SQLALCHEMY_DATABASE_URL
# DATABASE_URL = "sqlite:///./blog.db"
DATABASE_URL = "sqlite:///./data/blog.db"
# postgresql+psycopg2://user:password@localhost/db

# database type/driver → username : password → database host → PostgreSQL port (default) → database name
# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/fastapi-demo'

engine = create_engine(
    DATABASE_URL,
    # pool_size=20,
    # max_overflow=10,
    # pool_timeout=30,
    connect_args={"check_same_thread": False},  # needed only for SQLite
)

# ============ SESSION LOCAL ============ #
SessionLocal = sessionmaker(
    autocommit=False, # → DB not hit until commit() / flush()
    autoflush=False,
    bind=engine,
)

# AsyncSessionLocal = sessionmaker(
#     engine,
#     class_=AsyncSession,
#     expire_on_commit=False
# )

# ============ Declarative Base ============ #
# ORM mapping layer → Legacy
# Base = declarative_base() # Python classes ↔ Database tables.

# SQLAlchemy 2.0 model
# class Base(DeclarativeBase):
    # pass

# ============ INIT DB ============ #
def init_db():
    logger.info("Initializing database...")
    Base.metadata.create_all(bind=engine)

# ============ GET DB ============ #
def get_db(): # -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# async def get_db():
#     async with SessionLocal() as session:
#         yield session

# ============ CONTEXT MANAGER ============ #
# @contextmanager
# def get_scoped_db():
#     db = SessionLocal()
#     try:
#         yield db
#         db.commit()  # optional
#     except:
#         db.rollback()
#         raise
#     finally:
#         db.close()
