from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
# from typing import Generator
# from sqlalchemy.ext.asyncio import create_engine, session # create_async_engine, async_sessionmaker, AsyncSession

from app.db.base import Base
from app.core.logger import logger

from app.core.config import get_settings
settings = get_settings()

# SQLALCHEMY_DATABASE_URL
DATABASE_URL = settings.DATABASE_URL

# ---- SYNC ---- #
engine = create_engine(
    DATABASE_URL,
    # pool_size=20,
    # max_overflow=10,
    # pool_timeout=30,
    # pool_pre_ping=True, # Prevents stale connection errors in production.
    # connect_args={"check_same_thread": False},  # SQLite only
    # echo=True # Logs - settings.DEBUG
)

# ---- ASYNC ---- #
# engine = create_async_engine(
#     DATABASE_URL,
#     pool_size=10,
#     max_overflow=20,
#     pool_pre_ping=True,
# )

# ============ SESSION LOCAL ============ #
# ---- SYNC ---- #
SessionLocal = sessionmaker( 
    bind=engine,
    # autocommit=False, # → DB not hit until commit() / flush() | deprecated - always False now
    # autoflush=False, # special case
    expire_on_commit=False # Objects remain usable after commit.
)
# ---- ASYNC ---- #
# AsyncSessionLocal = async_sessionmaker(
#     bind=engine,
#     # class_=AsyncSession, # default
#     expire_on_commit=False
# )

# ============ INIT DB ============ #
def init_db():
    logger.info("Initializing database...")
    
    # Create tables (dev only)
    Base.metadata.create_all(bind=engine) 
    # models.Base.metadata.create_all(bind=engine)

# ============ GET DB ============ #
# ---- SYNC ---- #
def get_db(): # -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- ASYNC ---- #
# async def get_db():
#     async with AsyncSessionLocal() as db:
#         yield db

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
