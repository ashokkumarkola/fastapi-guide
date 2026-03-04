from fastapi import FastAPI, Header, Cookie, Query, Form, UploadFile
from pydantic import BaseModel, Field, HttpUrl, EmailStr, field_validator # PhoneNumber
from typing import Annotated, List, Optional

import phonenumbers
from enum import Enum
from uuid import UUID
from decimal import Decimal
from datetime import datetime, date, time, timedelta

# if TYPE_CHECKING:
#     from app.schemas.blog import Blog

class Image(BaseModel):
    # url: str
    
    # Special types
    # url: HttpUrl

    name: str

class Item(BaseModel):
    title: str
    description: str | None = None
    price: float
    tax: float | None = None
    # tags: list[str] = []
    tags: set[str] = set()

    # Nested Model
    image: Image | None = None

    # Lists of Submodels
    images: list[Image] | None = None

    # Header
    user_agent: Annotated[str | None, Header()] = None
    # headers: Annotated[CommonHeaders, Header()]

    # Cookie
    ads_id: Annotated[str | None, Cookie()] = None
    # cookies: Annotated[Cookies, Cookie()]

    # Request Example Data
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

    # class Config:
        # orm_mode = True # Deprecated
        # from_attributes = True # Modern

    # model_config = {
    #     'from_attributes': True
    # }

    # PydanticUserError: "Config" and "model_config" cannot be used together

# class Item(ItemBase):
#     model_config = {"from_attributes": True}
#     class Config:
#         from_attributes = True

# ---- ITEM BASE ---- #
# without Validation
class ItemBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    # cost: float
    quantity: int
    # tax: float | None = None
    category: str
    # tags: set[str] = set()
    image_url: str | None = None
    # images: list[Image] | None = None

# With Validation
class ItemBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    description: str | None = Field(None, max_length=1000)
    price: Decimal = Field(..., gt=0, decimal_places=2)
    quantity: int = Field(..., ge=0)
    category: str = Field(..., min_length=2, max_length=100)
    # image_url: str | None = None # HttpUrl
    is_active: bool = True

    # keep files outside Pydantic models | Pydantic models represent data structures, while files are transport-layer objects (UploadFile)
    # image: UploadFile | None = None

# ---- ITEM CREATE ---- #
class ItemCreate(ItemBase):
    model_config = {"extra": "forbid"}

# ---- ITEM UPDATE ---- #
# Full Update
class ItemFullUpdate(ItemBase):
    model_config = {"extra": "forbid"}

# Partial Update
class ItemUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=150)
    description: str | None = Field(None, max_length=1000)
    price: Decimal | None = Field(None, gt=0, decimal_places=2)
    quantity: int | None = Field(None, ge=0)
    category: str | None = Field(None, min_length=2, max_length=100)
    image_url: str | None = None # HttpUrl
    is_active: bool | None = True

# ---- ITEM RESPONSE ---- #
class ItemResponse(ItemBase):
    model_config = {"from_attributes": True}

    id: int
    image_url: str | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # @field_validator('total_value', mode='before')
    # @classmethod
    # def compute_total_value(cls, v, values) -> Decimal:
    #     price = values.data.get('price', 0)
    #     quantity = values.data.get('quantity', 0)
    #     return price * quantity

# ---- ITEM FILTER ---- #
class ItemFilter(BaseModel):
    pass
    # category: str | None = Query(None, description="Filter by category"),
    # min_price: float | None = Query(None, ge=0, description="Minimum price"),
    # max_price: float | None = Query(None, gt=0, description="Maximum price"),

# 
    # Editor support (completion, etc.), even for nested models
    # Data conversion
    # Data validation
    # Automatic documentation

class ItemStats(BaseModel):
    category: str
    avg_price: float

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[ItemBase]


# ---- FORM CREATE LEGACY ---- #
class ItemFormCreate(ItemBase):

    @classmethod
    def from_form(
        cls,
        name: str = Form(...),
        description: str | None = Form(None),
        price: Decimal = Form(...),
        quantity: int = Form(...),
        category: str = Form(...),
        image_url: str | None = Form(None),
        is_active: bool = Form(True),
    ):
        return cls(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            category=category,
            image_url=image_url,
            is_active=is_active,
        )

# ---- ERROR RESPONSE ---- #
class ErrorResponse(BaseModel):
    detail: str


    # blogs: List[Blog] = []
    # blogs: List["Blog"] = []


    # runtime import (important)
# from api.schemas.blog import BlogResponse

# model_rebuild resolves references
# UserResponse.update_forward_refs()# Pydantic v1
# UserResponse.model_rebuild() # Pydantic v2