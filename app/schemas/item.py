from fastapi import FastAPI, Header, Cookie, Query, Form, UploadFile
from pydantic import BaseModel, Field, HttpUrl, EmailStr, field_validator # PhoneNumber
from typing import Annotated, List, Optional

import phonenumbers
from enum import Enum
from uuid import UUID
from decimal import Decimal
from datetime import datetime, date, time, timedelta

class Image(BaseModel):
    # url: str
    
    # Special types
    # url: HttpUrl

    name: str

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

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

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[ItemBase]

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    quantity: int | None = None

class ItemResponse(ItemBase):
    id: int
    # owner_id: int
    # image_url: str | None
    class Config:
        from_attributes = True  # For SQLAlchemy compatibility

class ItemStats(BaseModel):
    category: str
    avg_price: float

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


class ItemFormData(BaseModel):
    model_config = {"extra": "forbid"}

    name: str
    price: float

# ---- FORM BASE ---- #
class ItemFormBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=150)
    description: str | None = Field(None, max_length=1000)
    price: Decimal = Field(..., gt=0, decimal_places=2)
    quantity: int = Field(..., ge=0)
    category: str = Field(..., min_length=2, max_length=100)
    image_url: HttpUrl | None = None
    is_active: bool = True

# ---- FORM CREATE ---- #
class ItemFormCreateLegacy(ItemFormBase):

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

class ItemFormCreate(ItemFormBase):
    pass

# 
class ItemFormUpdate(BaseModel):
    name: str | None = Field(None, min_length=2, max_length=150)
    description: str | None = Field(None, max_length=1000)
    price: Decimal | None = Field(None, gt=0, decimal_places=2)
    quantity: int | None = Field(None, ge=0)
    category: str | None = Field(None, min_length=2, max_length=100)
    image_url: HttpUrl | None = None
    is_active: bool | None = True

# ---- FORM RESPONSE ---- #
class ItemFormResponse(ItemFormBase):
    model_config = {"from_attributes": True}

    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # @field_validator('total_value', mode='before')
    # @classmethod
    # def compute_total_value(cls, v, values) -> Decimal:
    #     price = values.data.get('price', 0)
    #     quantity = values.data.get('quantity', 0)
    #     return price * quantity


# ---- ERROR RESPONSE ---- #
class ErrorResponse(BaseModel):
    detail: str
