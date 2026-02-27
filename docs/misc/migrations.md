# MIGRATIONS - ALEMBIC

## What & Why

> Migration = Version control for database schema

    - SQLAlchemy - how the database should look right now

    - ISSUE
        - can't just change a model
            (add column, change type, add index, rename table…) and restart the app
        - database would become incompatible with the old code / data

    - SOLUTION
        - keeps version history of schema changes
        - Generating small, repeatable Python scripts (upgrades + downgrades)
        - Allowing safe, controlled, auditable changes in dev → staging → production

## Basic Setup

### Step 0: Install dependencies

```bash
pip install alembic sqlalchemy[asyncio] asyncpg # if using PostgreSQL + async
```

### Step 1: Initialize Alembic

```bash
# Run in root: where main.py lives
alembic init alembic_migrations
```

```
alembic/
├── env.py
├── README
├── script.py.mako
└── versions/          ← future migration scripts will live here
alembic.ini
```

### Step 2: Configure alembic.ini

```bash
# sqlalchemy.url = driver://user:pass@host:port/dbname

# SQLite
sqlalchemy.url = sqlite:///./dev.db

# PostgreSQL:
sqlalchemy.url = postgresql+asyncpg://user:pass@localhost:5432/mydb
#               or postgresql+psycopg://... (sync)
```

### Step 3: Tell Alembic about your models (very important!)

- Edit alembic/env.py — near the bottom:

Find:

```py
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None
```

Replace with (adjust import path):

```py
# Assuming your models are in models/__init__.py or models/base.py
from src.db.base import Base   # ← your declarative_base()

target_metadata = Base.metadata
```

Also (recommended) — make DB URL dynamic:
Near top of env.py:

```py
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# this is the Alembic Config object
config = context.config

# Interpret the config file for Python logging...
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Add this block
from src.core.config import settings   # ← your settings (pydantic-settings or similar)
config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))
```

### Step 4: Create your first (empty) migration

```bash
alembic revision --autogenerate -m "initial schema"
```

Look inside alembic/versions/xxxx_initial_schema.py

You should see something like:

```py
def upgrade():
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    ...
    sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('items')
```

### Step 5: Apply it

```bash
alembic upgrade head
```

## The Flow – What Is Actually Happening?

```
You change model                  e.g. add Column('stock', Integer)
   ↓
alembic revision --autogenerate   compares models ↔ current DB
   ↓
creates new file in /versions/    with upgrade() + downgrade()
   ↓ (you review & possibly edit!)
alembic upgrade head              runs upgrade() of all pending revisions
   ↓
database schema is updated
   ↓
git commit migration file         ← very important!
   ↓
deploy → same command runs on prod
```

## Everyday Workflow

```bash
# Modify model
age = Column(Integer)

# Generate migration
alembic revision --autogenerate -m "add age column"

# Apply
alembic upgrade head
```

## Moderate / Standard Best Practices (2025–2026 style)

```
#,Practice,Why / When to use it,How to do it (code/snippet)
1,Use environment variables for DB URL,Never hardcode credentials,Use pydantic-settings or python-dotenv + os.getenv in env.py
2,Put Alembic in src/alembic or alembic/,Cleaner project structure,alembic init src/alembic
3,Use async driver if app is async,Consistency with FastAPI async endpoints,postgresql+asyncpg://... + create_async_engine in env.py
4,Always review & test auto-generated migrations,"Autogenerate misses renames, can produce dangerous ops","alembic revision --autogenerate, open file, check op. calls, test on copy of DB"
5,One logical change per migration,"Easier rollback, better history",Don't add 5 features in one file → make 5 small revisions
6,Commit migration files to git,Team must have same schema history,git add alembic/versions/
7,Never edit already applied migrations,Breaks history & prod,If mistake → create new revision that fixes it
8,Add naming conventions in env.py,"Better constraint/index names (ix_, fk_, ck_)","render_as_batch = True (sqlite), set naming_convention dict"
9,Run migrations before starting app in production,Prevents 500 errors on first requests,In Dockerfile / entrypoint: alembic upgrade head && uvicorn ...
10,Use --sql` mode for dry-run,See SQL without executing,alembic upgrade head --sql
11,Keep downgrade() realistic,Allows safe rollback in emergencies,Don't leave pass in downgrade
12,Use Docker Compose + Makefile,Standard dev/prod consistency,"make migrate, make upgrade, etc."
```
