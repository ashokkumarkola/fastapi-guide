# Setup and Configuration for FastAPI with PostgreSQL (SQLModel/SQLAlchemy)

## 1. Installing Dependencies

### Basics

To connect FastAPI to PostgreSQL, you need:

- An ORM or database toolkit: **SQLModel** (recommended for new FastAPI projects) or **SQLAlchemy**.
- A PostgreSQL driver: For async (preferred in FastAPI), use **asyncpg**; for sync or modern flexible use, **psycopg** (Psycopg 2, Psycopg 3+).

Common installation commands (using pip or uv in 2025):

```bash
# Core FastAPI
pip install fastapi uvicorn

# For SQLModel (includes SQLAlchemy 1.4+ and Pydantic integration)
pip install sqlmodel

# For pure SQLAlchemy (latest 2.0+)
pip install sqlalchemy

# Drivers
pip install asyncpg                  # Pure async, high performance
pip install psycopg, psycopg2
pip install psycopg[binary,pool]     # Modern Psycopg 3: sync/async compatible, recommended for flexibility

# Migrations
pip install alembic

# Environment management
pip install python-dotenv pydantic-settings  # For loading .env
```

### Advanced/Production Notes

- Use **psycopg** (not psycopg2) in 2025: It supports both sync and async modes, better pooling, and is the official successor.
- Avoid `psycopg2-binary` in production (it's for development; compile psycopg for better performance/security).
- For high-concurrency: `asyncpg` is often faster in benchmarks, but `psycopg` is easier to use and close in real-world FastAPI apps.
- Add `pydantic-settings` for typed config loading.

### Troubleshooting

- Driver not found: Ensure the driver matches your URL (e.g., `+asyncpg` requires asyncpg installed).
- Version conflicts: Pin versions if mixing SQLModel (ties to older SQLAlchemy) with latest features.

## 2. Environment Variables and `.env` Files for DATABASE_URL

### Basics

Never hardcode credentials. Use environment variables.

Create a `.env` file (gitignore it):

```env
# Async
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname

# Sync:
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/dbname
```

Load in code with `pydantic-settings`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str

    model_config = {"env_file": ".env"}

settings = Settings()
```

### Best Practices (Production-Ready)

- Use **secret management**: In Docker/K8s, inject via env; on cloud (Render, Railway), use their secret UI.
- Validate URL at startup.
- Separate dev/test/prod URLs.
- Add query params for tuning: `?pool_size=20&max_overflow=10`.

Example production config:

```python
from pydantic_settings import BaseSettings
from sqlalchemy import URL  # For safe building if needed

class Settings(BaseSettings):
    database_url: str  # Required

    @property
    def engine_url(self):
        return URL.create(self.database_url)  # Handles encoding

settings = Settings()
```

### Edge Cases/Troubleshooting

- Special chars in password (e.g., `@`, `/`): URL-encode or use `URL.create()`.
- Localhost vs remote: Add `?sslmode=require` for cloud DBs.
- Connection leaks: Always close pools on shutdown.

## 3. PostgreSQL Connection String Formats

### Basic Formats

- **Sync (default)**: `postgresql://user:password@host:port/dbname`
- **Async with asyncpg**: `postgresql+asyncpg://user:password@host:port/dbname`
- **Async/Sync with psycopg**: `postgresql+psycopg://user:password@host:port/dbname` (psycopg auto-detects async context in SQLAlchemy 2.0+)

Full example:

```text
postgresql+asyncpg://postgres:mypassword@localhost:5432/mydb?async_fallback=true
```

### Advanced Options (Query Params)

- Pooling: `pool_size=10&max_overflow=20&pool_timeout=30`
- Performance: `prepared_statements=true`
- SSL: `sslmode=require` or `sslcert=/path/to/cert`
- Schema search path: `options=-c%20search_path%3Dpublic,extensions`

### Best Practices

- Prefer `+asyncpg` or `+psycopg` for FastAPI (async framework).
- In 2025: `psycopg` is often recommended for new projects – unified sync/async, better error handling.

### Troubleshooting

- "Driver not found": Install matching package.
- Fallback issues: Add `async_fallback=true` for psycopg.
- Encoding errors: Use `URL.create()` to build safely.

## 4. Choosing Drivers: asyncpg vs psycopg (2025)

| Aspect                | asyncpg                                                           | psycopg (3+)                                         |
| --------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| **Performance**       | Often fastest raw (up to 3-5x in benchmarks for high concurrency) | Close second; real-world difference small in FastAPI |
| **Async Support**     | Native async only                                                 | Full async + sync in one library                     |
| **Ease of Use**       | Lower-level, manual pooling sometimes                             | Better pooling, Pydantic integration easier          |
| **SQLAlchemy Compat** | Excellent (2.0+)                                                  | Native support, future-proof                         |
| **Best For**          | Max throughput, pure async apps                                   | Most projects: flexibility, less boilerplate         |
| **Drawbacks**         | No sync mode; stricter API                                        | Slightly slower in extreme cases                     |

### Recommendations (2025)

- **Async FastAPI**: Start with `psycopg` (`+psycopg://`) – unified, modern.
- **Ultra-high concurrency**: `asyncpg` if benchmarks show gains.
- Avoid psycopg2 (legacy).

### Edge Cases

- Mixing sync/async code: psycopg handles gracefully; asyncpg blocks event loop if misused.
- Benchmarks: Test your workload – CPU-bound queries may favor sync.

## 5. Project Structure Best Practices

FastAPI doesn't enforce structure, but scalability demands separation of concerns.

### Small/Medium Projects (Flat by Type)

```
project/
├── app/
│   ├── main.py          # FastAPI app instance
│   ├── dependencies.py  # get_db, etc.
│   ├── models/          # SQLModel/SQLAlchemy models
│   ├── schemas/         # Pydantic input/output (if separate)
│   ├── crud/            # CRUD functions
│   ├── routers/         # APIRouter modules
│   ├── config.py        # Settings
│   └── database.py      # Engine, sessionmaker
├── alembic/             # Migrations
├── tests/
└── .env
```

### Large/Scalable Projects (Domain-Based – Recommended 2025)

Inspired by popular repos (e.g., zhanymkanov/fastapi-best-practices):

```
project/
├── src/
│   ├── core/            # Config, dependencies
│   ├── models/          # Shared models
│   ├── auth/            # Domain module
│   │   ├── router.py
│   │   ├── schemas.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   └── dependencies.py
│   ├── users/           # Another domain
│   │   └── ... (same pattern)
│   └── main.py
├── alembic/
└── tests/
```

### Production-Ready Tips

- **Separate schemas/models**: Models = DB, Schemas = API I/O.
- Add **services/** layer for business logic (keep routers thin).
- Use **lifespan** for startup/shutdown (pool management).
- Include **tests/** with dependency overrides for test DB.

### Edge Cases/Troubleshooting

- Circular imports: Use lazy imports or strings for relationships.
- Monolith vs microservices: Domain-based for large monoliths.
- Community Favorites (2025): Check full-stack-fastapi-template or zhanymkanov for starters.

This setup ensures maintainability, testability, and scalability in production.
