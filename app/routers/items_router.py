from typing import Annotated

from fastapi import FastAPI, APIRouter, Response, status
from pydantic import BaseModel

from enum import Enum
from datetime import datetime

from fastapi.responses import JSONResponse, RedirectResponse

"""
Field
Path
Query
Header
Cookie
Body
Form
File
"""

router = APIRouter(
    prefix='/items'
    tags='Items'
)

class Tags(Enum):
    items = "Items"
    users = "Users"

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

# GET ITEM
@router.get('/{item_id}', tags=['Items'],
    status_code=status.HTTP_200_OK,
    response_model=Item,
    response_model_exclude_unset=True,

    summary="Get an Item",
    description="Get an Item with all details", 
    response_description="Item Details"
)
def get_item(item_id: int) -> Item:
    return f"Item {item_id}" 

@router('/')
def read_items() -> list[Item]:
    return []

# CREATE ITEM
@router.post("/", response_description="The Created Item")
async def create_item(item: Item) -> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# DEPRECATED API
@router.get("/elements/", tags=["Items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]




# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# item: Item = Body(embed=True)
# item: Annotated[Item, Body(embed=True)]
