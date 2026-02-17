# BASE

## Why NOT define Base inside models.py

If you do this in multiple model files:

### products/models.py

class Base(DeclarativeBase): ...

### users/models.py

class Base(DeclarativeBase): ...

You now have:

❌ multiple Base.metadata
❌ tables not visible to each other
❌ create_all() creates partial schemas
❌ Alembic migrations break
