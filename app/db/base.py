from sqlalchemy.orm import declarative_base, DeclarativeBase

"""
Base = registry for models
All models must inherit SAME Base
Engine.create_all() uses Base.metadata
"""

# ============ Declarative Base ============ #
# ORM mapping layer → Legacy
# Base = declarative_base() # Python classes ↔ Database tables.

# SQLAlchemy 2.0 model
class Base(DeclarativeBase):
    pass
