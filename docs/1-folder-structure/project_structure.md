# Project Structure

## Folder Structure

```bash
myapp/
├── app/
│ ├── api/ # All route modules
│ │ ├── v1/
│ │ │ ├── **init**.py
│ │ │ ├── router.py
│ │ │ └── endpoints/
│ │ │ ├── users.py
│ │ │ └── items.py
│ ├── core/ # Config, security, events
│ │ ├── config.py
│ │ ├── security.py
│ │ └── events.py
│ ├── db/ # Database stuff
│ │ ├── session.py
│ │ └── base.py
│ ├── models/ # SQLAlchemy/Pydantic/Tortoise models
│ ├── schemas/ # Pydantic schemas (request/response)
│ ├── services/ # Business logic
│ ├── utils/ # Helpers, exceptions, etc.
│ └── main.py # FastAPI app instance + lifespan
├── tests/ # pytest + httpx
├── alembic/ # DB migrations (if using SQLAlchemy)
├── .env
├── .env.example
├── pyproject.toml # Best in 2025
└── Dockerfile
```

---

## For a Monolith

```bash
fastapi-project
├── alembic/
├── src
│ ├── auth
│ │ ├── router.py
│ │ ├── schemas.py # pydantic models
│ │ ├── models.py # db models
│ │ ├── dependencies.py
│ │ ├── config.py # local configs
│ │ ├── constants.py
│ │ ├── exceptions.py
│ │ ├── service.py
│ │ └── utils.py
│ ├── aws
│ │ ├── client.py # client model for external service communication
│ │ ├── schemas.py
│ │ ├── config.py
│ │ ├── constants.py
│ │ ├── exceptions.py
│ │ └── utils.py
│ └── posts
│ │ ├── router.py
│ │ ├── schemas.py
│ │ ├── models.py
│ │ ├── dependencies.py
│ │ ├── constants.py
│ │ ├── exceptions.py
│ │ ├── service.py
│ │ └── utils.py
│ ├── config.py # global configs
│ ├── models.py # global models
│ ├── exceptions.py # global exceptions
│ ├── pagination.py # global module e.g. pagination
│ ├── database.py # db connection related stuff
│ └── main.py
├── tests/
│ ├── auth
│ ├── aws
│ └── posts
├── templates/
│ └── index.html
├── requirements
│ ├── base.txt
│ ├── dev.txt
│ └── prod.txt
├── .env
├── .gitignore
├── logging.ini
└── alembic.ini

    - Store all domain directories inside src folder
        src/ - highest level of an app, contains common models, configs, and constants, etc.
        src/main.py - root of the project, which inits the FastAPI app
    - Each package has its own router, schemas, models, etc.
        router.py - is a core of each module with all the endpoints
        schemas.py - for pydantic models
        models.py - for db models
        service.py - module specific business logic
        dependencies.py - router dependencies
        constants.py - module specific constants and error codes
        config.py - e.g. env vars
        utils.py - non-business logic functions, e.g. response normalization, data enrichment, etc.
        exceptions.py - module specific exceptions, e.g. PostNotFound, InvalidUserData
    - When package requires services or dependencies or constants from other packages - import them with an explicit module name
```

---

## Import

```py
        from auth import constants as auth_constants
        from notifications import service as notification_service
        from posts.constants import ErrorCode as PostsErrorCode  # in case we have Standard ErrorCode in constants module of each package
```

---

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
