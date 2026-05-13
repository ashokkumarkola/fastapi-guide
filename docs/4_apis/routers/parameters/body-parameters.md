# FastAPI – Request Body

## Basics

- Request body → data **sent by client** to API
- Response body → data **sent by API** back to client
- Used mainly with: **POST, PUT, PATCH, DELETE**
- GET + body → discouraged / undefined behavior
- Declared using **Pydantic models** → validation + parsing + docs

---

## Pydantic BaseModel

- Import `BaseModel`
- Define data model with standard Python types
- Fields with default `None` → optional
- Required → fields with no default

```py
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
```

---

## Declaring Request Body

- Add Pydantic model as parameter
- FastAPI auto-recognizes → request body

```py
@app.post("/items/")
async def create_item(item: Item):
    return item
```

---

## FastAPI Automatic Features

- Read JSON request body
- Type conversion
- Data validation
- Clear error messages
- Editor support (autocomplete, type checks)
- Generates JSON Schema
- Included in OpenAPI docs

---

## Model Usage Inside Function

- Access attributes directly
- `.model_dump()` (Pydantic v2) / `.dict()` (v1)
- Example with computed fields:

```py
item_dict = item.dict()
if item.tax is not None:
    item_dict.update({"price_with_tax": item.price + item.tax})
```

---

## Request Body + Path Parameters

- Both can be used together
- Path parameters → taken from URL
- Pydantic model → taken from body

```py
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
```

---

## Request Body + Path + Query Parameters

- All three types can be combined
- FastAPI distinguishes automatically:

  - Path parameters → from URL
  - Simple types (str, int, bool) → query
  - Pydantic model → request body

```py
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
```

---

## Required vs Optional

- No default → **required**
- `= None` → **optional**
- Type annotation does NOT make it optional — **default value does**

---

## Editor Support

- Type hints → autocomplete
- Pydantic plugin for PyCharm → validation, refactor tools
- Strong typing → fewer bugs

---

## Without Pydantic

- Possible using `Body(...)`
- Useful for singular values or advanced cases
- But Pydantic recommended → validation + clarity

---

## Summary – FastAPI + Request Body Superpowers

- Pydantic models → structured data
- Automatic:

  - parsing
  - validation
  - JSON schema
  - error messages
  - documentation

- Clean endpoint definitions
- High editor productivity

---
