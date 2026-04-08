# Engine and Connection Management in FastAPI with PostgreSQL (SQLModel/SQLAlchemy)

## 1. Creating the Engine (`create_engine` for Sync, `create_async_engine` for Async)

### Basics

The **Engine** is the core interface to the database in SQLAlchemy/SQLModel. It manages the connection pool and dialect-specific behavior.

- **Sync Engine** (SQLAlchemy 2.0+):

  ```python
  from sqlalchemy import create_engine

  engine = create_engine("postgresql+psycopg://user:pass@host:5432/dbname")
  ```

  - Uses synchronous drivers (e.g., `psycopg` or legacy `psycopg2`).

- **Async Engine** (Recommended for FastAPI):

  ```python
  from sqlalchemy.ext.asyncio import create_async_engine

  engine = create_async_engine("postgresql+asyncpg://user:pass@host:5432/dbname")
  # or with modern psycopg (unified sync/async):
  engine = create_async_engine("postgresql+psycopg://user:pass@host:5432/dbname")
  ```

  - Requires async drivers: `asyncpg` (pure async, high performance) or `psycopg` (flexible sync/async in one lib).
  - Engine creation is lazy: No actual DB connection until first use.

### Advanced

- Use `URL.create()` for safe URL building (handles password encoding):

  ```python
  from sqlalchemy import URL

  url = URL.create(
      drivername="postgresql+asyncpg",
      username="user",
      password="pass@with/special#chars",
      host="localhost",
      port=5432,
      database="mydb"
  )
  engine = create_async_engine(url)
  ```

### Best Practices (Production-Ready)

- Create **one global engine** per database (share the pool).
- Prefer async engine in FastAPI for non-blocking I/O.
- In 2025: Use `psycopg` driver (`postgresql+psycopg://`) for most projects – unified, modern, excellent pooling.

### Edge Cases/Troubleshooting

- "No driver found": Install matching package (`pip install asyncpg` or `psycopg`).
- Special chars in credentials: Always use `URL.create()`.
- Mixing sync/async: Avoid sync engine in async FastAPI (blocks event loop).

## 2. Engine Options (echo=True, future=True, pool_size, connect_args)

### Key Options (SQLAlchemy 2.0+ as of Dec 2025)

Pass as kwargs to `create_engine` / `create_async_engine`:

| Option            | Description                                                            | Default | Production Recommendation            |
| ----------------- | ---------------------------------------------------------------------- | ------- | ------------------------------------ |
| **echo**          | Log SQL statements (`True` or `"debug"` for results)                   | False   | `False` (use logging module instead) |
| **future**        | Deprecated in 2.0+ (all engines are "future" style)                    | True    | Omit (will be removed)               |
| **pool_size**     | Persistent connections in pool                                         | 5       | 10-20+ based on load                 |
| **max_overflow**  | Temporary extra connections allowed                                    | 10      | 10-50 (monitor exhaustion)           |
| **pool_timeout**  | Seconds to wait for connection checkout                                | 30      | 10-30 (fail fast)                    |
| **pool_recycle**  | Recycle connections after N seconds (prevents stale)                   | -1      | 3600 (for MySQL-like disconnects)    |
| **pool_pre_ping** | Test connection liveness on checkout                                   | False   | `True` (robust disconnect handling)  |
| **pool_use_lifo** | Use Last-In-First-Out (faster recent connections)                      | False   | `True` often better                  |
| **connect_args**  | Dict passed directly to DBAPI `connect()` (e.g., SSL, server_settings) | {}      | Common for PostgreSQL                |

Example production engine:

```python
engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_size=20,
    max_overflow=40,
    pool_timeout=30,
    pool_pre_ping=True,
    pool_use_lifo=True,
    pool_recycle=3600,
    connect_args={"server_settings": {"jit": "off"}}  # PostgreSQL-specific example
)
```

PostgreSQL-specific `connect_args`:

- SSL: `{"sslmode": "require"}`
- Schema search path: `{"server_settings": {"search_path": "myschema,public"}}`

### Best Practices

- Tune pooling based on concurrency (Uvicorn workers + async tasks).
- Enable `pool_pre_ping=True` in production for auto-reconnect.
- Use structured logging (not `echo=True`).

### Troubleshooting

- Connection timeouts: Lower `pool_timeout` or increase `pool_size`.
- Stale connections: Set `pool_recycle`.
- High load leaks: Monitor with `echo_pool="debug"`.

## 3. Connection Pooling

### Basics

SQLAlchemy uses **QueuePool** by default (async: **AsyncAdaptedQueuePool**):

- Maintains `pool_size` persistent connections.
- Allows `max_overflow` temporary extras (closed after use).
- Connections recycled/reused efficiently.

### Advanced Differences (Sync vs Async)

- Sync: Thread-safe, FIFO/LIFO queue.
- Async: Awaitable checkout, no blocking.
- No pre-creation: Connections created on demand.

Special pools:

- `NullPool`: No pooling (useful with PgBouncer transaction mode).
- `SingletonThreadPool`: For SQLite.

### Best Practices (Production)

- Share one engine/pool globally.
- For PgBouncer (transaction pooling): Use `NullPool` to avoid double-pooling.
- Monitor: Use `echo_pool="debug"` temporarily or tools like pg_top.

### Edge Cases/Troubleshooting

- Overflows: "QueuePool limit reached" → Increase size/overflow or optimize queries.
- Leaks: Always close sessions/connections; use `async with`.
- Multi-process (Uvicorn workers): Each worker has own pool → Scale `pool_size` accordingly.

## 4. Lifespan Events in FastAPI for Engine Initialization/Shutdown

### Basics

FastAPI's **lifespan** (preferred over deprecated `@app.on_event`) handles startup/shutdown.

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

engine: AsyncEngine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    global engine
    engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
    app.state.engine = engine  # Share via app.state
    yield
    # Shutdown
    await engine.dispose()  # Critical for async!

app = FastAPI(lifespan=lifespan)
```

### Production-Ready Pattern (with Session Factory)

```python
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_async_engine(DATABASE_URL, pool_pre_ping=True)
    AsyncSessionLocal.configure(bind=engine)  # Rebind if needed
    app.state.db_engine = engine
    yield
    await engine.dispose()
```

Dependency for routes:

```python
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
```

### Best Practices

- Create engine in lifespan startup.
- Always `await engine.dispose()` on shutdown (prevents RuntimeError in GC).
- Store engine/sessionmaker in `app.state`.
- Use for other resources (caches, ML models).

### Edge Cases/Troubleshooting

- No dispose: Warnings like "Event loop is closed".
- Multi-loop sharing: Use `NullPool` or dispose/recreate.
- Testing: Override lifespan or use TestClient with custom app.

## 5. Switching from SQLite (Tutorial) to PostgreSQL (Production)

### Basics

FastAPI/SQLModel tutorials use SQLite for simplicity:

```python
# Tutorial (SQLite)
engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
```

Switch to PostgreSQL:

- Change URL: `"postgresql+asyncpg://user:pass@host:5432/dbname"`
- Remove SQLite-specific `connect_args`.
- Use async engine.

### Why Switch?

- SQLite: File-based, no concurrency limits → Great for dev/tests.
- PostgreSQL: Client-server, robust concurrency, features (JSONB, full-text), production-ready.

### Production-Ready Steps

1. Use env var for URL (dev: SQLite, prod: PostgreSQL).
2. Migrations: Alembic (configure for async if needed).
3. Docker: Separate PostgreSQL container.
4. No code changes needed beyond URL/engine if models are standard.

Example env-based:

```python
if settings.ENV == "development":
    engine = create_engine("sqlite:///./dev.db")
else:
    engine = create_async_engine(settings.DATABASE_URL)  # postgresql+asyncpg://...
```

### Edge Cases/Troubleshooting

- Schema differences: PostgreSQL case-sensitive; use quoted identifiers if needed.
- Concurrency: SQLite locks file → Switch early to catch issues.
- Data types: Minor differences (e.g., BOOLEAN handling).
- Testing: Use PostgreSQL test DB or SQLite with overrides.

This configuration ensures scalable, reliable database access in production while keeping development simple.
