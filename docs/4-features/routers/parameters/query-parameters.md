# FastAPI – Query Parameters

## Basics

- Non-path parameters → automatically **query parameters**
- Located after `?` in URL → `?skip=0&limit=10`
- Passed to function by name
- Type hints → parsing + validation + editor support + auto docs

---

## Defaults

- Query params can be **optional**
- Defaults applied when not provided
- Example:
  - `/items/?skip=20` → `skip=20`, `limit=10` (default)

---

## Optional Query Parameters

- Default `None` → optional
- FastAPI auto-detects path vs query
- Only non-path params become query params

```py
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    ...
```

---

## Bool Conversion

- Converts typical truthy/falsey strings
- Accepted as `True`:

  - `1`, `true`, `True`, `on`, `yes`

- Any other → `False`

```py
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    ...
```

---

## Multiple Path + Query Params

- Any mix of path + query parameters
- Order in function doesn’t matter
- FastAPI detects by name

```py
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    ...
```

---

## Required Query Parameters

- No default value → **required**
- Missing param → validation error

```py
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    ...
```

- Error if missing → `{"detail":[{"type":"missing",...}]}`
- Must provide: `/items/foo?needy=value`

---

## Mixed Requirements

- Combine required, defaulted, optional params

```py
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    ...
```

- `needy`: required
- `skip`: default
- `limit`: optional

---

## Enum Support

- Query params can also use Enums
- Same rules as path params
- Enforces predefined values
- Better docs + stricter validation

---

## Summary – FastAPI Advantages

- Type hints →

  - Parsing
  - Validation
  - Documentation

- Automatic conversion: int, bool, optional types
- Clear error messages
- No boilerplate → FastAPI handles everything behind the scenes

---
