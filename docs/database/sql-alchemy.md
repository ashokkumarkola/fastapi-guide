# Database

- sqlalchemy will not create db, it uses db

# Install

pip install sqlalchemy

# Establishing Connectivity - the Engine

from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

What kind of database are we communicating with?

What DBAPI are we using?
postgressql, sqlite3

How do we locate the database?
url

**Lazy Initialization** - Lazy Connecting: First time performed task against db
