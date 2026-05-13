# Modern Python (3.6+)

> Write Less • Read More • Build Faster

---

# Why Modern Python?

- Cleaner Syntax
- Faster Development
- Better Async Support
- Strong Typing
- Production Ready
- Huge Ecosystem

---

# Python 3.6 Highlights

## f-Strings 🔥

```python
name = "Ashok"
print(f"Hello {name}")
```

- Fast
- Clean
- Readable

---

## Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

- Better IDE support
- Safer code
- Easier debugging

---

## Underscores in Numbers

```python
price = 1_000_000
```

Readable large numbers.

---

# Python 3.7 Highlights

## Dataclasses ⚡

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

- Less boilerplate
- Auto `__init__`
- Cleaner models

---

## Dictionary Order Guaranteed

```python
dict preserves insertion order
```

Useful for APIs & JSON.

---

# Python 3.8 Highlights

## Walrus Operator :=

```python
if (n := len(data)) > 10:
    print(n)
```

Assign + use together.

---

## Positional Only Params

```python
def add(a, b, /):
    pass
```

API safety.

---

# Python 3.9 Highlights

## Merge Dictionaries

```python
x = a | b
```

Simple & elegant.

---

## Built-in Generic Types

```python
list[str]
dict[str, int]
```

No need for `typing.List`.

---

# Python 3.10 Highlights

## Match Case 🚀

```python
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
```

Python switch-case.

---

## Better Union Types

```python
str | None
```

Cleaner typing.

---

# Python 3.11 Highlights

## Much Faster ⚡⚡

- Huge speed improvements
- Better error messages
- Faster startup

---

## Exception Groups

```python
except* ValueError:
```

Useful in async apps.

---

# Python 3.12 Highlights

## Cleaner Generics

```python
class Box[T]:
    pass
```

Modern typing syntax.

---

## Faster Again 🚀

Python keeps getting faster.

---

# Must Know Features

## List Comprehension

```python
squares = [x*x for x in range(5)]
```

---

## Lambda Functions

```python
lambda x: x * 2
```

---

## Enumerate

```python
for i, val in enumerate(items):
```

---

## Zip

```python
for a, b in zip(x, y):
```

---

## Context Managers

```python
with open("a.txt") as f:
    pass
```

Auto cleanup.

---

## Decorators

```python
@login_required
def home():
    pass
```

Function modifiers.

---

## Generators

```python
yield value
```

Memory efficient loops.

---

# Async Python ⚡

## Async / Await

```python
async def main():
    await task()
```

Core of:

- FastAPI
- Async APIs
- High concurrency

---

# Modern Typing

## Optional

```python
str | None
```

---

## Typed Dict

```python
from typing import TypedDict
```

---

## Literal Types

```python
Literal["GET", "POST"]
```

---

## Protocols

Duck typing with types.

---

# Virtual Environments

```bash
python -m venv venv

source venv/bin/activate
```

Always isolate projects.

---

# Package Management

## pip

```bash
pip install fastapi
```

---

## Modern Tools

- pip
- uv ⚡
- poetry
- hatch

---

# Modern Project Structure

```text
project/
│
├── app/
├── tests/
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

# pyproject.toml ❤️

Modern Python config file.

Used for:

- dependencies
- formatting
- linting
- packaging

---

# Important Tools

## Formatter

- black

## Linter

- ruff

## Type Checker

- mypy

## Testing

- pytest

---

# Testing

```python
def test_add():
    assert add(1, 2) == 3
```

---

# API & Backend Stack

## Most Popular

- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- PostgreSQL
- Redis

---

# Performance Tips

- Use async wisely
- Avoid blocking code
- Use generators
- Cache expensive tasks

---

# Golden Rules 🏆

- Readability > Cleverness
- Explicit > Implicit
- Small Functions
- Type Everything
- Write Tests
- Keep It Simple

---

# Python Zen

```python
import this
```

---

# Best Python Versions

## Recommended

- Python 3.11 ✅
- Python 3.12 ✅

Avoid old versions unless required.

---

# Learn Order

1. Basics
2. OOP
3. Functions
4. Modules
5. Virtual Env
6. Async
7. Typing
8. APIs
9. Databases
10. Testing

---

# For FastAPI 🚀

Must Know:

- async/await
- typing
- dataclasses
- pydantic
- generators
- decorators
- dependency injection basics

---

# One Line Summary

> Modern Python = Clean Syntax + Async Power + Strong Typing + Fast Development

```

```
