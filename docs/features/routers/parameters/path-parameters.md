# FastAPI – Path Parameters

## Basics

- Path parameters = variables inside URL
- Python format-style: `/items/{item_id}`
- Auto-passed to function as arguments
- Direct browser test → `/items/foo` → `{"item_id":"foo"}`

---

## Typed Path Parameters

- Use Python type hints: `item_id: int`
- Editor support: autocomplete, type checks
- Auto data parsing → `"3"` → `3` (int)
- Auto validation → invalid types → structured HTTP error

---

## Validation Behavior

- Wrong type → detailed error (`int_parsing`)
- Shows: location, expected type, offending input
- Helps debugging & client clarity

---

## Auto Documentation

- `/docs` → Swagger UI
- `/redoc` → ReDoc alternative
- Type hints → documented parameter types
- Based on OpenAPI → tool compatibility, code generation

---

## Pydantic Integration

- Under-the-hood validation
- Supports: `str`, `int`, `float`, `bool`, complex types
- Consistent request parsing and error handling

---

## Order Matters

- Path operations evaluated top-down
- Define fixed path _before_ dynamic path
  - `/users/me`
  - `/users/{user_id}`
- Duplicate paths → first one always wins

---

## Predefined Values (Enum)

- Use Python `Enum` for fixed allowed values
- Creates strict path parameter choices
- Improves docs → shows selectable values
- Enum member usage:
  - Compare: `model_name is ModelName.alexnet`
  - Get value: `model_name.value`
- FastAPI auto-converts enum → JSON string

---

## Returning Enum Members

- Return enum in response → auto-converted to value
- Example JSON:
  ```json
  { "model_name": "alexnet", "message": "Deep Learning FTW!" }
  ```

## Path Parameters Containing Paths

- Need nested paths: `/files/{file_path}`
- Use Starlette path converter:

  - `/files/{file_path:path}`

- Matches entire path including `/home/user/file.txt`
- Leading slash → requires double slash in URL

---

## Recap – FastAPI Advantages

- Type hints →

  - Editor support
  - Auto parsing
  - Auto validation
  - Auto documentation

- Declare once → used everywhere
- Big differentiator vs other frameworks
- High performance + strong developer experience
