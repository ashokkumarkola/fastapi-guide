from pydantic import BaseModel, EmailStr, Field
from typing import List, TYPE_CHECKING, Optional
# from .Blog import BlogMain
from datetime import datetime

# if TYPE_CHECKING:
#     from app.schemas.blog import Blog

# -------- BASE SCHEMA -------- #
class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=50)
    full_name: str | None = None
    # is_active: bool | None = True
    # is_veirifed: str
    # created_at: datetime
    # updated_at: datetime
class User(UserBase):
    class Config:
        from_attributes = True

# -------- CREATE SCHEMA -------- #
class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

# -------- UPDATE SCHEMA -------- #
class UserUpdate(UserBase):
    password: str = Field(min_length=6)
    bio: Optional[str] = None
    phone_number: Optional[str] = None
    profile_photo: Optional[str] = None
    is_active: Optional[bool] = None

# -------- PARTIAL UPDATE SCHEMA -------- #
class UserPartialUpdate(BaseModel):
    email: EmailStr | None= None
    username: str | None = None
    full_name: str | None = None
    password: str | None = None
    phone_number: str | None = None
    bio: str | None = None

# -------- RESPONSE SCHEMA -------- #
class UserResponse(UserBase):
    id: int
    phone_number: str | None = None
    bio: str | None = None
    is_active: bool
    is_verified: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime | None = None
    last_login: datetime | None = None

    # blogs: List[Blog] = []
    # blogs: List["Blog"] = []

    class Config:
        from_attributes = True

class UserSuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: UserResponse | None = None # Any

class UserErrorResponse(BaseModel):    
    success: bool = False 
    message: str 
    error_code: str | None = None

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

# -------- AUTH SCHEMA -------- #
class CurrentUser(UserResponse):
    is_superuser: bool

class Login(BaseModel):
    username: str
    password: str

# -------- RESPONSE SCHEMA -------- #
class BulkUserCreate(BaseModel):
    users: List[UserCreate]

class BulkUserResponse(BaseModel):
    message: str
    count: int
    users: List[UserResponse]

# runtime import (important)
# from api.schemas.blog import BlogResponse

# model_rebuild resolves references
# UserResponse.update_forward_refs()# Pydantic v1
# UserResponse.model_rebuild() # Pydantic v2
