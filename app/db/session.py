# from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import ( 
    create_async_engine, 
    async_sessionmaker, 
    AsyncSession
)

from app.db.base import Base
from app.core.logger import logger

from app.core.database import engine
from app.core.config.config import get_settings
settings = get_settings()

# SQLALCHEMY_DATABASE_URL
DATABASE_URL = settings.DATABASE_URL


# =========================================================
# SYNC SESSION 
# =========================================================

# ======== SYNC SESSION FACTORY ======== #
SessionLocal = sessionmaker( 
    bind=engine,
    class_=Session,
    autocommit=False,  # control transactions manually | DB not hit until commit() / flush() | deprecated - always False now
    autoflush=False,   # prevents unexpected automatic flushes
    expire_on_commit=False # Without this ORM objects expire after commit
)

# ============ INIT DB ============ #
def init_db():
    logger.info("Initializing database...")
    
    # Create tables (dev only)
    Base.metadata.create_all(bind=engine) 
    # models.Base.metadata.create_all(bind=engine)

# ======== SYNC DATABASE SESSION DEPENDENCY - GET DB ======== #
def get_db(): # -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ============ CONTEXT MANAGER ============ #
# scripts background jobs cron tasks CLI tools worker systems
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

# def create_db_and_tables():
#     SQLModel.metadata.create_all(engine)


# =========================================================
# ASYNC SESSION 
# =========================================================

# ======== ASYNC SESSION FACTORY ======== #
# AsyncSessionLocal = async_sessionmaker(
#     bind=engine,

#     class_=AsyncSession,

#     autoflush=False,

#     autocommit=False,

#     expire_on_commit=False,
# )


# ======== ASYNC DATABASE SESSION DEPENDENCY ======== #
# async def get_db():
#     async with AsyncSessionLocal() as session:
#         try:
#             yield session

#             await session.commit()

#         except Exception:
#             await session.rollback()
#             raise

#         finally:
#             await session.close()