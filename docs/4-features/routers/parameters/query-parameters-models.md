# FastAPI – Query Parameter Models

## Purpose

- Allows grouping related query params into a **Pydantic model**
- Useful when many related query params exist
- Re-use model across multiple endpoints
- Declare **validations + metadata** in one place
- Supported since **FastAPI ≥ 0.115.0** :contentReference[oaicite:1]{index=1}

---

## Query Parameters with a Pydantic Model

- Define a Pydantic model with fields representing query params
- Use `Annotated[Model, Query()]` in endpoint signature

```py
from typing import Annotated, Literal
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
```

- Fields automatically extracted from query string
- Validation rules apply (`gt`, `le`, `ge`, literal choices, etc.) ([FastAPI][1])

---

## Model Field Validations

- Use Pydantic **Field()** to enforce:

  - numeric ranges (`gt`, `ge`, `le`)
  - default values
  - field types (`list[str]`, `Literal[...]`)

- FastAPI auto applies these validations to query params ([FastAPI][1])

---

## Multiple Syntax Variants

- Annotated version (preferred)
- Legacy non-Annotated version:

```py
@app.get("/items/")
async def read_items(filter_query: FilterParams = Query()):
    return filter_query
```

- Both work — **Annotated** is recommended for clarity + editor support

---

## Check the Docs

- Query param fields from the model show in:

  - `/docs` → Swagger UI
  - `/redoc` → ReDoc UI

- Example values and validations appear automatically

---

## Forbid Extra Query Parameters

- You can restrict query parameters to only those defined in the model
- Use Pydantic model config:

```py
class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query
```

- Sending unknown query params → validation error: `extra_forbidden` ([FastAPI][1])

---

## Summary

- Pydantic models for query params enable:

  - grouped parameter definitions
  - shared validation and metadata
  - reuse across endpoints
  - better code structure and type safety

- Works with `Query()` + `Annotated` for best clarity ([FastAPI][1])

---
