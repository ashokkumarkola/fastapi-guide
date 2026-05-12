from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Index,
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
    id = Column(Integer, primary_key=True, index=True) # autoincrement=True

    # AUTHENTICATION IDENTITY
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False) # password_hash - hashed password

    # PROFILE INFORMATION
    full_name = Column(String(100), nullable=True) # name
    bio = Column(Text, nullable=True)
    phone_number = Column(String(20), unique=True, index=True, nullable=True)
    profile_photo = Column(String(500), nullable=True)

    # Ecommerce/customer fields
    # role = Column(String(20), nullable=False, default="customer", server_default="customer")

    # ACCOUNT STATUS & VERIFICATION 
    is_active = Column(Boolean, nullable=False, default=True) # server_default=text("true")
    is_verified = Column(Boolean, nullable=False, default=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    # TIMESTAMPS & AUDIT FIELDS
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=True) # False

    last_login = Column(DateTime(timezone=True), nullable=True) # server_default=func.now()
    # deleted_at = Column(DateTime(timezone=True), nullable=True)

    # email_verified_at = Column(DateTime(timezone=True), nullable=True)
    # phone_verified_at = Column(DateTime(timezone=True), nullable=True)

    # account lockout/rate-limit flows after repeated bad logins.
    # failed_login_attempts = Column(Integer, nullable=False, default=0, server_default="0")
    # locked_until = Column(DateTime(timezone=True), nullable=True)

    # __table_args__ = (
    #     CheckConstraint("length(username) >= 3", name="check_users_username_min_length"),
    #     CheckConstraint(
    #         "role IN ('customer', 'staff', 'admin')",
    #         name="check_users_role_allowed",
    #     ),
    #     Index("ix_users_email_username", "email", "username"),
    # )

    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, email={self.email!r}, username={self.username!r})"
