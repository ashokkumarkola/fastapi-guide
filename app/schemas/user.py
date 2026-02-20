from pydantic import BaseModel
from typing import List, TYPE_CHECKING
# from .Blog import BlogMain
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.blog import Blog

class UserBase(BaseModel):
    name: str
    email: str
    password: str
    # first_name: str
    # last_name: str
    # is_veirifed: str
    # created_at: datetime
    # updated_at: datetime

class User(UserBase):
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: str | None = None

class UserResponse(BaseModel):
    # id: int
    name: str
    email: str
    # password: str

    # blogs: List[Blog] = []
    # blogs: List["Blog"] = []

    class Config:
        orm_mode = True

    # model_config = {
    #     'from_attributes': True
    # }

# runtime import (important)
# from api.schemas.blog import BlogResponse

# model_rebuild resolves references
# UserResponse.update_forward_refs()# Pydantic v1
# UserResponse.model_rebuild() # Pydantic v2

class Login(BaseModel):
    username: str
    password: str

