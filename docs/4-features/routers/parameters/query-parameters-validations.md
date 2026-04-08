# FastAPI – Query Parameters & String Validations

## Basics

- Function params not in path → **query parameters**
- Optional when default value exists
- `str | None` → editor support + optional
- Type hints → parsing, validation, docs

```py
async def read_items(q: str | None = None):
```

---

## Additional Validation

- Use **Annotated** + **Query()** for validation metadata
- Requires FastAPI ≥ 0.95.0

```py
q: Annotated[str | None, Query(max_length=50)] = None
```

---

## Import Requirements

- `from typing import Annotated`
- `from fastapi import Query`

---

## Why Annotated

- Cleaner default values
- Real Python defaults kept
- Better editor support
- Multi-metadata support
- Avoids confusion between Query default vs function default
- Recommended over legacy Query-as-default style

---

## Legacy (Old) Style

```py
q: str | None = Query(default=None, max_length=50)
```

- Still works, but less recommended

---

## More Validations

### Min Length

```py
q: Annotated[str | None, Query(min_length=3, max_length=50)] = None
```

### Pattern (Regex)

```py
q: Annotated[
    str | None,
    Query(min_length=3, max_length=50, pattern="^fixedquery$")
] = None
```

### (Deprecated) regex

- Old name before Pydantic v2
- Use **pattern** instead

---

## Default Values

```py
q: Annotated[str, Query(min_length=3)] = "fixedquery"
```

- Any default makes parameter optional

---

## Required Parameter

```py
q: Annotated[str, Query(min_length=3)]
```

- No default → required

---

## Required but Accepts None

```py
q: Annotated[str | None, Query(min_length=3)]
```

- Must be provided
- Value may be `None`

---

## Multiple Values (List)

```py
q: Annotated[list[str] | None, Query()] = None
```

URL:

```
/items/?q=foo&q=bar
```

Default list:

```py
q: Annotated[list[str], Query()] = ["foo", "bar"]
```

List without content validation:

```py
q: Annotated[list, Query()] = []
```

---

## Metadata Additions

### Title

```py
Query(title="Query string")
```

### Description

```py
Query(description="Search string for matching items", min_length=3)
```

### Alias

```py
q: Annotated[str | None, Query(alias="item-query")] = None
```

### Deprecated

```py
Query(deprecated=True)
```

### Exclude from OpenAPI

```py
Query(include_in_schema=False)
```

---

## Custom Validation – AfterValidator (Pydantic v2)

```py
from pydantic import AfterValidator

def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError("Invalid ID format")
    return id

id: Annotated[str | None, AfterValidator(check_valid_id)] = None
```

Key points:

- Custom validation after normal validation
- Only for local data checks
- For DB/API checks → use **Dependencies**

---

## Summary – Validation Tools

### Generic:

- **alias**
- **title**
- **description**
- **deprecated**
- **include_in_schema**

### String-specific:

- **min_length**
- **max_length**
- **pattern**

### Custom:

- **AfterValidator**

FastAPI + Annotated + Query → powerful, clear, fully documented query validation.

```

```
