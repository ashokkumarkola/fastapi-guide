# ------------------------------
# IMPORTS
# ------------------------------

from sqlalchemy import (
    # String types
    String, Text, CHAR, VARCHAR, CLOB,

    # Numeric types
    Integer, BigInteger, SmallInteger,
    # Float, Numeric, Decimal,

    # Boolean & Binary
    Boolean, LargeBinary, BLOB,

    # Date/Time
    # DateTime, Date, Time, TIMESTAMP,

    # Special types
    # JSON, ARRAY, Enum, PickleType, UUID,

    # Constraints
    # Index, CheckConstraint, UniqueConstraint,
    # PrimaryKeyConstraint, ForeignKeyConstraint,

    # 
    Column, ForeignKey
)

# ORM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# PostgreSQL extensions
# from sqlalchemy.dialects.postgresql import JSONB, UUID as PG_UUID

# MySQL extensions
# from sqlalchemy.dialects.mysql import YEAR, LONGTEXT

from datetime import datetime
from decimal import Decimal
from uuid import uuid4

from app.database import Base

# ------------------------------
# DECLARATIVE BASE
# ------------------------------

# Python models ↔ SQLAlchemy ORM metadata

# SQLAlchemy 1.0
# Base = declarative_base()

# SQLAlchemy 2.0
# class Base(DeclarativeBase):
#     pass

# ------------------------------
# MODELS
# ------------------------------

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    blogs = relationship("Blog", back_populates="creator")
