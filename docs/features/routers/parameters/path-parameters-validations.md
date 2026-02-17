# FastAPI – Path Parameters & Numeric Validations

## Basics

- Use `Path()` to add metadata/validation to path parameters
- Works like `Query()` but for path params (required by default)
- Import:
  ```py
  from fastapi import Path
  from typing import Annotated
  ```

---

## Using Annotated (Recommended)

- Wrap type with `Annotated[type, Path(...)]`
- Cleaner defaults + metadata
- Example:
  ```py
  item_id: Annotated[int, Path(title="The ID of the item to get")]
  ```

---

## Path Metadata

- You can document path params like:
  - `title`
  - `description`
  - `example`
- This information appears in OpenAPI / docs UI :contentReference[oaicite:3]{index=3}

---

## Numeric Validations

### Common constraints

- `ge` → greater than or equal
- `gt` → greater than
- `le` → less than or equal
- `lt` → less than
- Works on ints and floats :contentReference[oaicite:4]{index=4}

### Examples

- Integer >= 1:

  ```py
  item_id: Annotated[int, Path(ge=1)]

  ```

- Range constraint:

  ```py
  item_id: Annotated[int, Path(gt=0, le=1000)]
  ```

- Float with lower & upper limits:
  ```py
  size: Annotated[float, Query(gt=0, lt=10.5)]
  ```

---

## Mixing Path & Query Validations

- You can combine `Path()` and `Query()` in same endpoint
- FastAPI will correctly validate both path and query params
- Example uses both in one function :contentReference[oaicite:8]{index=8}

---

## Using Defaults & Order

- Path params always required (no default unless specified)
- Python default rules apply if mixing with other params
- Order doesn’t matter for FastAPI extraction, but Python enforces correct default/required ordering :contentReference[oaicite:9]{index=9}

---

## Legacy (Non-Annotated) Style

- Instead of `Annotated`, you can specify `= Path(...)` directly
- E.g.:
  ```py
  item_id: int = Path(title="The ID of the item")
  ```

* Works but `Annotated` is cleaner and recommended ([FastAPI][1])

---

## Summary

- `Path()` allows **metadata + validation** on path params
- Numeric validations: **ge, gt, le, lt**
- Combine with `Query()` for richer parameter definitions
- Annotated style is preferred for clarity and editor support ([FastAPI][1])

---
