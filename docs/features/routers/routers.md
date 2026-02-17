# ROUTERS

## async def vs def

- `async def`: I/O-bound operations (like DB calls).
- `def`: CPU-intensive work or if your database library is not async.

---

## Tags

tags=["Products"] is not for routing logic,
but for documentation grouping in your API’s interactive docs and OpenAPI schema.

---

## Return Format for Production

Always use response_model.
It ensures data validation, filters sensitive fields, and auto-generates accurate API docs.
Do not return ORM models directly.

---

## Session vs AsyncSession

Use AsyncSession with async database drivers (e.g., asyncpg).
Use Session for traditional sync drivers.
They are not interchangeable.

---

## Exception Blocks

Do not use generic try/except in every endpoint.
Use FastAPI's HTTPException for known errors and global exception handlers for a clean, consistent API

---

async router api - async service - async dao -

db sesson for every method in class or for whole class in init
which one best and production

## The Core Principle: The Async "Chain of Await"

You need async in the router, service, and DAO because they form a call chain where each level must await the next. A single await in the DAO requires everything above it to also be async.

```py
# ❌ This WILL NOT WORK: Async breaks at the service layer
@router.get("/{id}")                     # async def  <-- OK
async def get_product(...):
    result = product_service.get(id)     # ❌ BLOCKING! Should be 'await'
    return result

class ProductService:
    def get(self, id: int):              # ❌ NORMAL def <-- PROBLEM!
        product = product_dao.get(id)    # ❌ Can't 'await' here!
        return product

class ProductDAO:
    async def get(self, id: int):        # ✅ ASYNC def
        return await self.db.get(Product, id)  # ✅ Awaits database

# ✅ This WORKS: Async all the way through
@router.get("/{id}")                     # ✅ async def
async def get_product(...):
    result = await product_service.get(id)  # ✅ Awaits service
    return result

class ProductService:
    async def get(self, id: int):        # ✅ async def
        product = await product_dao.get(id)  # ✅ Awaits DAO
        # Can add async business logic here
        return product

class ProductDAO:
    async def get(self, id: int):        # ✅ async def
        return await self.db.get(Product, id)  # ✅ Awaits database
```
