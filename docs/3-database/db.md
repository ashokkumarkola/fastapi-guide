### 1. Setup and Configuration

- Installing dependencies (e.g., `sqlmodel`, `sqlalchemy`, `asyncpg`, `psycopg`, `alembic`)
- Environment variables and `.env` files for DATABASE_URL
- PostgreSQL connection string formats (sync: `postgresql://`, async: `postgresql+asyncpg://` or `postgresql+psycopg://`)
- Choosing drivers (asyncpg for async, psycopg for modern sync/async)
- Project structure best practices (separating config, models, schemas, routers)

### 2. SQLModel vs SQLAlchemy

- Differences between SQLModel and pure SQLAlchemy
- When to use SQLModel (simpler, Pydantic integration, recommended in FastAPI docs)
- When to use SQLAlchemy (more mature, complex queries, better documentation for edge cases)
- Hybrid approaches (using both)
- SQLModel limitations (e.g., incomplete docs, older SQLAlchemy version support in some cases)

### 3. Engine and Connection Management

- Creating the engine (`create_engine` for sync, `create_async_engine` for async)
- Engine options (echo=True, future=True, pool_size, connect_args)
- Connection pooling
- Lifespan events in FastAPI for engine initialization/shutdown
- Switching from SQLite (tutorial) to PostgreSQL (production)

### 4. Models and Schema Definition

- Defining models (SQLModel classes with `table=True`, SQLAlchemy DeclarativeBase)
- Fields and columns (Field, Column, primary_key, index, relationships)
- Type annotations and Pydantic integration
- Input/Output schemas (separate Pydantic models vs reusing SQLModel)
- Relationships (one-to-many, many-to-many)
- Table arguments (indexes, constraints, schemas)

### 5. Sessions and Dependencies

- Session creation (`Session` for sync, `AsyncSession` for async)
- Sessionmaker and async_sessionmaker
- Dependency injection with `Depends` (e.g., `get_session` or `get_db`)
- Yielding sessions for per-request scoping
- Session lifecycle (commit, rollback, refresh, close)

### 6. CRUD Operations

- Creating records (add, commit, refresh)
- Reading data (select, filters, get, first, all)
- Updating records
- Deleting records
- Query building (where, order_by, limit, offset, joins)
- Executing raw SQL when needed

### 7. Synchronous vs Asynchronous

- Sync setup with SQLAlchemy/SQLModel
- Async setup (AsyncEngine, AsyncSession, async drivers)
- Benefits of async for high concurrency
- Mixing sync and async (avoiding blocking the event loop)
- Performance considerations

### 8. Migrations

- Setting up Alembic
- Configuring Alembic for async engines
- Autogenerate revisions
- Upgrading/downgrading database
- Integrating migrations in startup or CLI

### 9. Advanced Features

- Relationships and eager/lazy loading
- Transactions and nesting
- Events and listeners
- Multiple databases/engines
- Schema support in PostgreSQL
- Bulk operations

### 10. Testing and Development

- Testing database interactions (overriding dependencies)
- Using test databases
- Fixtures for sessions
- Dropping/creating tables in tests
- Debugging queries (echo mode)

### 11. Production Best Practices

- Security (connection limits, SSL, credentials management)
- Error handling (HTTP exceptions, integrity errors)
- Pagination and filtering
- Validation with Pydantic
- Docker integration with PostgreSQL
- Monitoring and logging queries

### 12. Official Resources and Templates

- FastAPI official SQL databases tutorial
- Full-stack FastAPI PostgreSQL template
- SQLModel documentation
- SQLAlchemy documentation for advanced use
- Common patterns from community (e.g., service layer, repositories)
