from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, TYPE_CHECKING, Optional
from datetime import datetime
from app.utils.validations import validate_phone

# -------- BASE SCHEMA -------- #
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str | None = None

    # phone_number: str | None = Field(None, pattern=r"^\+?[0-9]{10,15}$")
    # @field_validator("phone_number")
    # @classmethod
    # def validate_phone(cls, value):
    #     if value is None:
    #         return value
    #     if validate_phone(value):
    #         return value

# -------- CREATE SCHEMA -------- #
class UserCreate(UserBase):
    model_config = {"extra": "forbid"}

    password: str = Field(..., min_length=8)

# -------- UPDATE SCHEMA -------- #
class UserUpdate(UserBase):
    model_config = {"extra": "forbid"}

    password: str = Field(..., min_length=8, max_length=128)
    phone_number: str | None = None
    bio: str | None = None
    profile_photo: str | None = None
    is_active: bool | None = None

# -------- PARTIAL UPDATE SCHEMA -------- #
class UserPartialUpdate(BaseModel):
    model_config = {"extra": "forbid"}

    email: EmailStr | None= None
    username: str | None = None
    full_name: str | None = None
    password: str | None = None
    phone_number: str | None = None
    bio: str | None = None
    profile_photo: str | None = None
    is_active: bool | None = None

    @field_validator("phone_number")
    @classmethod
    def validate_phone(cls, value):
        if value is None:
            return value
        if validate_phone(value):
            return value

# -------- RESPONSE SCHEMA -------- #
class UserResponse(UserBase):
    model_config = {"from_attributes": True}

    id: int
    phone_number: str | None = None
    bio: str | None = None
    is_active: bool
    is_verified: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime | None = None
    last_login: datetime | None = None

class UserSuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: UserResponse | None = None

class UserErrorResponse(BaseModel):    
    success: bool = False 
    message: str 
    error_code: str | None = None

# -------- CURRENT USER -------- #
class CurrentUser(UserResponse):
    is_superuser: bool

# -------- FILTER SCHEMA -------- #
class UsersPaginated(BaseModel):
    total: int
    page: int
    size: int
    users: List[UserResponse]    

class UserQueryParams(BaseModel):
    page: int = Field(default=1, ge=1)
    size: int = Field(default=10, ge=1, le=100)

    search: str | None = None
    email: str | None = None

    sort_by: str = "id"
    order: str = "asc"

# -------- BULK RESPONSE SCHEMA -------- #
class BulkUserCreate(BaseModel):
    users: List[UserCreate]

class BulkUserResponse(BaseModel):
    message: str
    count: int
    users: List[UserResponse]

# -------- AUTH SCHEMA -------- #
class Login(BaseModel):
    email: str
    password: str
