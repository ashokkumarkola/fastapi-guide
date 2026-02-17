from pydantic import BaseModel, Field
from typing import List, TYPE_CHECKING
# from user import User

if TYPE_CHECKING:
    from app.schemas.user import User
    # from .user import User


# Field Validations in Pydantic Models
# Field(
#     default=None, title="The description of the item", 
#     min_length=3, max_length=50, 
#     gt=0, lt=100, ge=0, le=100,
    
# )


class BlogBase(BaseModel):
    title: str
    content: str
    published: bool = False

class Blog(BlogBase):
    class Config:
        orm_mode = True

class BlogCreate(BaseModel):
    title: str
    content: str
    published: bool = False

class BlogUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    published: bool | None = None

class BlogResponse(BlogCreate):
    id: int

    # creator: User
    # creator: "User"

    # SQLAlchemy -> Pydantic
    class Config:
        orm_mode = True

# runtime import (important)
# from api.schemas.user import UserResponse
# BlogResponse.model_rebuild()
