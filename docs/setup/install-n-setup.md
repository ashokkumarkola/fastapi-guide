# Create Project Folder

```bash
mkdir fastapi-guide
cd fastapi-guide
```

---

# Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate

# Add .gitignore
echo "*" > .venv/.gitignore

# Deactivate the Virtual Environment
deactivate
```

---

# Install Libraries

```bash
# minimal setup
pip intstall fastapi uvicorn

# full-feature setup - recommended
pip intstall 'fastapi[standard]' 'uvicorn[standard]'

# db
pip install sqlalchemy psycopg2 asyncpg sqlmodel

# validation
pip install pydantic pydantic-settings

# View all installed libraries
pip list
pip show lib_name
```

---

#

```bash
# Modern Dependencies (pyproject.toml in 2025)
[project]
name = "myapp"
dependencies = [
    "fastapi[standard]>=0.115",
    "uvicorn[standard]>=0.30",
    "sqlmodel>=0.0.18",             # or pydantic-settings + sqlalchemy
    "alembic>=1.13",
    "python-jose[cryptography]",
    "passlib[bcrypt]",
    "python-multipart",             # for form data / file uploads
    "email-validator",
]

[project.optional-dependencies]
dev = ["pytest", "httpx", "pytest-cov", "ruff", "mypy", "pre-commit"]

[tool.uvicorn]
reload = true
```

---

#
