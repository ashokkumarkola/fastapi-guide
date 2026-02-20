from fastapi import FastAPI, Header, Cookie
from pydantic import BaseModel, Field # HttpUrl, PhoneNuber, EmailStr
from typing import Annotated, List

from enum import Enum
from uuid import UUID
from datetime import datetime, date, time, timedelta

class Image(BaseModel):
    # url: str
    
    # Special types
    url: HttpUrl

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
    name: str
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
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }

class ItemBase(BaseModel):
    name: str
    description: str | None = Field(default=None, title="The description of the item", max_length=300)
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[ItemBase]



class ItemIn(BaseModel):
    name: str

class ItemOut(BaseModel):
    name: str



class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


# 
    # Editor support (completion, etc.), even for nested models
    # Data conversion
    # Data validation
    # Automatic documentation


