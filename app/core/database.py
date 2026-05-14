from sqlalchemy import text
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import (
    # AsyncSession,
    # async_sessionmaker,
    create_async_engine,
)

from app.core.config.config import get_settings
settings = get_settings()

# SQLALCHEMY_DATABASE_URL
DATABASE_URL = settings.DATABASE_URL


# =========================================================
# SYNC ENGINE
# =========================================================

# ======== CREATE SYNC ENGINE ======== #
engine = create_engine(
    url=str(DATABASE_URL),

    # SQL logging
    echo=False,

    # Connection pooling
    # pool_size=settings.database.pool_size,

    # max_overflow=settings.database.max_overflow,

    # pool_timeout=settings.database.pool_timeout,

    # pool_recycle=settings.database.pool_recycle,

    # pool_pre_ping=settings.database.pool_pre_ping,

    # SQLAlchemy 2.0 behavior
    future=True,
)


# =========================================================
# ASYNC ENGINE
# =========================================================

# ======== CREATE ASYNC ENGINE ======== #
# engine = create_async_engine(
#     url=str(settings.database.url),

#     # SQL logging
#     echo=settings.database.echo,

#     # Connection pooling
#     pool_size=settings.database.pool_size,

#     max_overflow=settings.database.max_overflow,

#     pool_timeout=settings.database.pool_timeout,

#     pool_recycle=settings.database.pool_recycle,

#     pool_pre_ping=settings.database.pool_pre_ping,

#     # SQLAlchemy 2.0 behavior
#     future=True,
# )

# async def check_db_connection():
#     async with engine.begin() as conn:
#         await conn.execute(text("SELECT 1"))


# #########################################################
# automatic session lifecycle
# automatic rollback safety
# automatic cleanup
# clean architecture