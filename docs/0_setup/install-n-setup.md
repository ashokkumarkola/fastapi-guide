# Project Setup

> FastAPI Environment & Dependency Setup

---

## Create Project

```bash
# Create folder
mkdir fastapi-guide

# Enter project
cd fastapi-guide
```

---

## Virtual Environment

- `isolated runtime environment`

```bash
# Create venv
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows CMD)
venv\Scripts\activate

# Activate (PowerShell)
.\venv\Scripts\Activate.ps1

# Deactivate
deactivate
```

---

## Verify Environment

```bash
# Python path
which python

# Pip path
which pip

# Installed packages
pip list
pip show lib_name
```

---

## .gitignore

```bash
# Create .gitignore
touch .gitignore
```

```text
# Python
__pycache__/
*.pyc

# Virtual env
venv/

# Environment
.env

# Testing
.pytest_cache/
```

---

## Upgrade pip

```bash
# Upgrade pip
pip install --upgrade pip
```

---

# Install FastAPI

## Minimal Setup

```bash
# FastAPI + Uvicorn
pip install fastapi uvicorn
```

---

## Recommended Setup

```bash
# Full featured install
pip install "fastapi[standard]" "uvicorn[standard]"
```

---

# Database Libraries

```bash
# PostgreSQL sync driver
pip install psycopg2-binary

# PostgreSQL async driver
pip install asyncpg

# ORM
pip install sqlalchemy

# SQLModel
pip install sqlmodel

# Migrations
pip install alembic
```

---

# Validation & Config

```bash
# Validation
pip install pydantic

# Settings management
pip install pydantic-settings

# Environment variables
pip install python-dotenv
```

---

# Security Libraries

```bash
# JWT
pip install python-jose[cryptography]

# Password hashing
pip install passlib[bcrypt]
```

---

# Development Tools

```bash
# Linter + formatter
pip install ruff

# Testing
pip install pytest pytest-cov

# Type checking
pip install mypy

# API testing
pip install httpx
```

---

# Useful pip Commands

```bash
# List packages
pip list

# Package details
pip show fastapi

# Freeze dependencies
pip freeze

# Generate requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

---

# Modern Setup With uv

## Install uv

```bash
# Install uv
pip install uv
```

---

## Initialize Project

```bash
# Initialize project
uv init

# Create venv
uv venv
```

---

## Install Packages

```bash
# FastAPI
uv add fastapi uvicorn

# Database stack
uv add sqlalchemy asyncpg alembic

# Dev tools
uv add --dev ruff pytest mypy
```

---

## Run Application

```bash
# Run server
uv run uvicorn app.main:app --reload
```

---

# Recommended Initial Stack

```bash
# Production-ready setup
pip install \
fastapi[standard] \
uvicorn[standard] \
sqlalchemy \
asyncpg \
alembic \
pydantic-settings \
python-jose[cryptography] \
passlib[bcrypt] \
ruff \
pytest
```

---

# Verify Installation

```bash
# FastAPI version
python -c "import fastapi; print(fastapi.__version__)"

# Uvicorn version
uvicorn --version
```

---

# Recommended Structure

```text
fastapi-guide/
├── app/
├── tests/
├── venv/
├── .env
├── .gitignore
├── requirements.txt
└── pyproject.toml
```

---

# Best Practices

## Use

- Virtual environments
- pyproject.toml
- .env files
- Separate configs
- Dev dependencies

---

## Avoid

- Global installs
- Hardcoded secrets
- Mixed environments
- Untracked dependencies

<!-- # Create Project Folder

```bash
mkdir fastapi-guide
cd fastapi-guide
```

---

# Virtual Environment

- `isolated runtime environment`

```bash
# Create
python3 -m venv venv

# Activate
source venv/bin/activate

# Deactivate
deactivate

# Add .gitignore
echo "venv" > .gitignore
```

---

# Install Libraries

```bash
# minimal setup
pip install fastapi uvicorn

# full-feature setup - recommended
pip install 'fastapi[standard]' 'uvicorn[standard]'

# db
pip install sqlalchemy psycopg2 asyncpg sqlmodel

# validation
pip install pydantic pydantic-settings

# View all installed libraries
pip list
pip show lib_name
```

--- -->
