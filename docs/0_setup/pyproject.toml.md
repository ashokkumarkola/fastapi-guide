# pyproject.toml

> Modern Python Project Config

---

## Why

Centralized config for:

- Dependencies
- Build system
- Tool settings
- Project metadata

---

## Replaces

- requirements.txt
- setup.py
- setup.cfg
- pytest.ini
- tox.ini
- MANIFEST.in

---

## Python Standards

- PEP 518
- PEP 621

---

## Modern Stack

### Recommended Tools

- uv
- Poetry
- Hatch
- PDM

---

## Basic Structure

```toml
[project]
name = "myapp"
version = "0.1.0"

dependencies = [
    "fastapi",
    "uvicorn"
]
```

---

## Build System

```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

---

## Tool Config

### Ruff

```toml
[tool.ruff]
line-length = 100
```

---

## FastAPI Example

```toml
[project]
name = "fastapi-app"

dependencies = [
    "fastapi",
    "uvicorn[standard]"
]
```

---

## Modern Dependency Setup

```bash
# Install uv Globally
pip install uv

# Init Project
uv init

# Add Packages
uv add fastapi uvicorn

# Add Database Stack
uv add sqlalchemy psycopg[binary] alembic

# Add Dev Tools
uv add --dev ruff pytest mypy
```

---

## Run Server

```bash
uv run uvicorn app.main:app --reload
```

---

## Ruff Commands

```bash
# Check
uv run ruff check .

# Auto Fix
ruff check . --fix

# Format
uv run ruff format .
```

---

## Production Dependencies

```toml
[project]
dependencies = [
    "fastapi[standard]>=0.115",
    "uvicorn[standard]>=0.30",
    "sqlmodel>=0.0.18",
    "alembic>=1.13",
    "python-jose[cryptography]",
    "passlib[bcrypt]",
    "python-multipart",
    "email-validator",
]
```

---

## Dev Dependencies

```toml
[project.optional-dependencies]

dev = [
    "pytest",
    "pytest-cov",
    "httpx",
    "ruff",
    "mypy",
    "pre-commit"
]
```

---

## Uvicorn Config

```toml
[tool.uvicorn]
reload = true
```

---

## Poetry Setup

```bash
# Create Project
poetry new my-fastapi-app

# Install Packages
poetry add fastapi uvicorn
```

---

## Existing Project Migration

### Convert

```bash
poetry init
```

---

## Current Best Practice

### New Projects

- pyproject.toml
- uv / Poetry
- Ruff
- Typed dependencies

### Legacy Projects

- requirements.txt

---

## Key Idea

```text
Single Source Of Truth
```
