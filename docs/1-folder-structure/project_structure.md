# PROJECT STRUCTURE

## FEATURES

- models
- schemas
- router
- service
- dao
- exceptions
- dependencies
- utils
- constants
- responses

---

## Import

```py
from auth import constants as auth_constants
from notifications import service as notification_service
from posts.constants import ErrorCode as PostsErrorCode  # in case we have Standard ErrorCode in constants module of each package
```

---

```bash
# models.py → DB structure only
SQLAlchemy tables
No business logic
No Pydantic
✔️ Product ORM model only

# schemas.py → API contracts
Request / response shapes
Validation rules
Serialization (from_attributes)
✔️ ProductCreate, ProductResponse

# dao.py → Pure DB operations (CRUDE, no logic)
Only SQLAlchemy queries
No FastAPI
No HTTPException
No validation
No business rules

✔️ Examples:
insert_product
fetch_product_by_id
fetch_products
delete_product

❌ Never:
Raise HTTP errors
Check permissions
Apply business rules

# service.py → Business logic layer
Uses DAO
Applies rules
Decides what to do

✔️ Examples:
Check duplicates
Handle not-found
Soft delete logic
Transform data

# exceptions.py → Centralized API errors
All HTTPException creators
Reusable & consistent
✔️ product_not_found()

# dependencies.py → Dependency injection
DB session
Auth user
Permissions
✔️ get_db()

# router.py → HTTP only
Routes
Status codes
Depends
Request/response models

❌ No SQL
❌ No business rules

# constants.py → Static values
Table names
Error messages
Limits
Enums

✔️ PRODUCT_TABLE = "products"

# utils.py → Pure helpers
Formatting
Slug generation
Calculations

❌ No DB
❌ No FastAPI
```

---

## Tips

```bash
# Copy Folder structure to file
tree > file_name

tree -L <number>
```

---

## Reference

zhanymkanov: fastapi-best-practices
https://github.com/zhanymkanov/fastapi-best-practices/blob/master/README.md#pydantic

---
