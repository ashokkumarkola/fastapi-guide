from fastapi import FastAPI, Header, Cookie, Query
from pydantic import BaseModel, Field # HttpUrl, PhoneNuber, EmailStr
from typing import Annotated, List, Optional

from enum import Enum
from uuid import UUID
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


