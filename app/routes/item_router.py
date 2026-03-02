from fastapi import FastAPI, APIRouter, Response, status, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel

from enum import Enum
from datetime import datetime
from typing import Annotated

from fastapi.responses import JSONResponse, RedirectResponse

from app.services.item_service import ItemService

from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse, ItemFilter
from app.db.session import get_db

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
    prefix='/items',
    tags=['Items']
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

@router.get('/{item_id}', 
    # tags=['Items'], 
    deprecated=True

    # status_code=status.HTTP_200_OK,
    # response_model=ItemResponse,
    # response_model_exclude_unset=True,
    # responses={404: {'model': ErrorResponse}}

    # summary="Get an Item",
    # description="Get an Item with all details", 
    # response_description="Item Details"
)
def get_item(item_id: int, response: Response, db: Session = Depends(get_db)) -> ItemResponse:
    item = ItemService.get_item(db, item_id)

    # Custom headers
    response.headers["X-Total-Count"] = str(len(item))
    response.headers["X-Custom-Meta"] = "Processed"  # Example

    return item

#  GET ITEM 
@router.get('/{item_id}', status_code=status.HTTP_200_OK, response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)) -> ItemResponse:
    return ItemService.get_item(db, item_id)

#  LIST ITEMS 
@router.get('/', status_code=status.HTTP_200_OK, response_model=list[ItemResponse])
def get_items(
    db: Session = Depends(get_db)
) -> list[ItemResponse]:
    """
    Retrieve items with optional filters.
    - **category**: Exact match.
    - **min_price/max_price**: Range filter.
    Raises 400 if invalid params.
    """
    return ItemService.get_items(db)

#  CREATE ITEM 
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ItemResponse)
async def create_item(item: ItemCreate, db: Session = Depends(get_db)): # -> ItemResponse:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return ItemService.create_item(db, item)

#  UPDATE ITEM 
@router.put("/", response_model=ItemResponse)
async def update_item(item_id: int, updates: ItemUpdate, db: Session = Depends(get_db)):
    item = ItemService.update_item(db, item_id, updates)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item

#  UPDATE ITEM PARTIALLY 
@router.patch("/", response_model=ItemResponse)
async def update_item(item_id: int, updates: ItemUpdate, db: Session = Depends(get_db)):
    item = ItemService.update_item(db, item_id, updates)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return item

#  DELETE ITEM 
@router.delete("/", status_code=status.HTTP_404_NOT_FOUND)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = ItemService.delete_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return {"message": "Deleted"}

# SOFT DELETE ITEM
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, deprecated=True)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = ItemService.delete_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return {"message": "Deleted"}

# FILTER ITEM 
@router.get("/filter/category", status_code=status.HTTP_200_OK, response_model=list[ItemResponse])
async def get_filter_items(
    # category: str | None = None,
    category: str | None = Query(None, description="Filter by category"),
    min_price: float | None = Query(None, ge=0, description="Minimum price"),
    max_price: float | None = Query(None, gt=0, description="Maximum price"),
    # filters: ItemFilter | None = None,
    db: Session = Depends(get_db)
) -> list[ItemResponse]:
    if min_price is not None and max_price is not None and min_price > max_price: 
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="min_price cannot be greater than max_price"
        ) 
    
    items = ItemService.get_filter_items(db, category, min_price, max_price) 

    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="No items found with applied filters"
        ) 
    
    return items 

# PATCH /items/{id}/restore

# BULK CREATE
@router.post("/bulk", status_code=status.HTTP_201_CREATED, response_model=list[ItemResponse])
async def create_bulk_items(items=list[ItemCreate], db: Session = Depends(get_db)):
    pass

# DELETE /items/bulk
# PATCH /items/{id}/status

# ITEM STATS
@router.get("/stats/avg_price")
async def get_item_category_avg_price_stats(db: Session = Depends(get_db)):
    """
    Aggregate stats: average price by category.
    """
    stats = ItemService.get_item_category_avg_price_stats(db)
    if not stats:
        return []
    
    return [{"category": cat, "avg_price": float(avg)} for cat, avg in stats]

# DEPRECATED API
@router.get("/elements", deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]




# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# item: Item = Body(embed=True)
# item: Annotated[Item, Body(embed=True)]


# Request → Router
    # JSON data
    # {
    #     "key": "value",
    #     "key": "value"
    # }

    # to 
        # obj: PydanticSchema

    # Pydantic model instance
    # key='value' key='value'

# Router → Service
    # Pydantic model instance
    # key='value' key='value'

    # to
        # obj..dict()

    # Dict
    # {
    #     "key": "value",
    #     "key": "value"
    # }


# DAO → SQLAlchemy Model

    # Dict
        # {
        #     "key": "value",
        #     "key": "value"
        # }

    # to
        # Item(**data)
        
    # SQLAlchemy object 
        # {
        #     "key": "value",
        #     "key": "value"
        # }

# Database → Response
    # SQLAlchemy object is persisted in the database.
    # Returned object is serialized back into a Pydantic response schema.
    # Final output: JSON response sent to the client.