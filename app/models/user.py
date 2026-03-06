from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Text
)
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    """
        User Table
    """
     
    __tablename__ = "users"

    # PRIMARY KEY
    id = Column(Integer, primary_key=True, index=True)

    # AUTHENTICATION FIELDS
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False) # hashed password

    # PROFILE INFORMATION
    full_name = Column(String)
    bio = Column(Text, nullable=True)
    profile_photo = Column(String, nullable=True)
    phone_number = Column(String(20), nullable=True)

    # USER STATUS FLAGS
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)

    # TIMESTAMPS
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=True) # False

    last_login = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
