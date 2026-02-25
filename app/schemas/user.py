from pydantic import BaseModel, EmailStr, Field
from typing import List, TYPE_CHECKING, Optional
# from .Blog import BlogMain
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.blog import Blog

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

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserUpdate(UserBase):
    password: str = Field(min_length=6)

class UserPartialUpdate(BaseModel):
    email: EmailStr | None= None
    username: str | None = None
    full_name: str | None = None
    password: str | None = None

class UserResponse(UserBase):
    id: int
    created_at: datetime

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

# 
class CurrentUser(UserResponse):
    is_superuser: bool

class Login(BaseModel):
    username: str
    password: str

# 
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
