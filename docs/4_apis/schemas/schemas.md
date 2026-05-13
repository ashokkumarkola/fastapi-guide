## BaseModel

Schema ≠ Model

Layer Purpose
Pydantic Schema Validate + serialize API input/output
SQLAlchemy Model Persist data in DB
Service Layer Business rules
Router HTTP concerns

Schema defines the contract. Model defines storage.

What it does

Core class of Pydantic

Provides:

Runtime data validation

Type coercion

Serialization (dict(), json())

OpenAPI schema generation

Why it exists

Converts untrusted input (JSON) → trusted Python objects

ProductCreate(price="10") # becomes float(10.0)

---

## ENTERPRISE-GRADE FOLDER STRUCTURE

app/
├── api/
│ ├── v1/
│ │ ├── products/
│ │ │ ├── router.py
│ │ │ ├── schemas.py
│ │ │ ├── service.py
│ │ │ └── dependencies.py
│ │ └── **init**.py
│ └── **init**.py
│
├── core/
│ ├── database.py
│ ├── config.py
│ └── security.py
│
├── models/
│ ├── product.py
│ └── base.py
│
├── migrations/
│ └── alembic/
│
└── main.py

✔ Versioned APIs
✔ Domain-based
✔ Scales to 50+ modules

---

## Field(...)

Field adds metadata + validation rules.

... (Ellipsis)

```py
name: str = Field(...)
```

Means:

Required field

Missing → validation error

Equivalent to:

```py
name: str
```

but Field(...) lets you attach constraints.

---

## Schema Inheritance (Create vs Response)

class ProductResponse(ProductCreate):
id: int

What happens

ProductResponse contains:

All fields of ProductCreate

Plus id

Why this pattern

Avoid duplication

Ensure response is superset of create schema

Industry standard naming

## Config.from_attributes = True (Pydantic v2)

Why required

Pydantic v2 does not auto-read ORM attributes.

product = ProductORM(...)
ProductResponse.model_validate(product)

Without:
❌ Error
With:
✅ Reads attributes like product.id, product.name

v1 vs v2
Version Setting
v1 orm_mode = True
v2 from_attributes = True

## ORM ↔ Pydantic Mapping

Layer Responsibility
SQLAlchemy DB structure & persistence
Pydantic Validation & serialization
Golden rule
❌ Never reuse ORM models as API schemas

- Convert ORM → Pydantic → Client

### Best-Practice Schema Separation

```
ProductCreate     # input
ProductUpdate     # partial input
ProductResponse   # output
```

Why?

    Security (hide internal fields)

    API evolution

    Validation differences

## Alternative & Improved Validation Styles

### Using Annotated (Recommended)

from typing import Annotated
from pydantic import Field

Name = Annotated[str, Field(max_length=100)]

name: Name

✔ Cleaner
✔ Reusable
✔ Type-checker friendly

### from pydantic import constr, conint, confloat

name: constr(max_length=100)
price: confloat(gt=0)
quantity: conint(ge=0)

⚠️ Less flexible in v2
✅ Still valid

### ataclasses vs BaseModel

Use case Choice
API schemas BaseModel
Internal logic dataclasses
DTOs BaseModel

## Production Best Practices

### Naming Conventions

ProductCreate → POST
ProductUpdate → PATCH
ProductResponse → GET

### Required vs Default

Required → Field(...)

Optional → default value

Nullable → | None

### Enums for Category

from enum import Enum

class Category(str, Enum):
ELECTRONICS = "electronics"
FOOD = "food"

category: Category

✔ Prevent invalid values
✔ Clean OpenAPI

### OpenAPI Metadata

Field(
...,
max_length=100,
description="Product name",
example="iPhone 15"
)

---

## Gotchas & Edge Cases

### Floating-point price ❌

price: float

⚠️ Precision bugs

Correct
from decimal import Decimal
price: Decimal

### Nullable vs Empty String

description: str | None

None ≠ ""

Enforce explicitly if needed

### Validation error customization

@field_validator("price")
@classmethod
def price_check(cls, v):
if v > 1_000_000:
raise ValueError("Price too high")
return v

### Pydantic v1 → v2 migration traps

@validator → @field_validator

orm_mode removed

.dict() → .model_dump()

## Advanced Patterns

### Custom Validators

@field_validator("name")
@classmethod
def strip_name(cls, v):
return v.strip()

### Nested Schemas

class CategoryOut(BaseModel):
id: int
name: str

### Schema Evolution

Add fields with defaults

Never remove fields abruptly

Version APIs (/v1, /v2)

### Response Envelope

class APIResponse(BaseModel):
data: ProductResponse
meta: dict

FastAPI Integration
@app.post("/products", response_model=ProductResponse)
async def create_product(payload: ProductCreate):
...

✔ Automatic validation
✔ Automatic docs
✔ Automatic serialization

### 🧠 Final Mental Model

SQLAlchemy

Controls how data is stored

Pydantic

Controls how data enters and leaves your system

Best teams

Keep them separate

Type everything

Validate aggressively

Evolve schemas carefully
