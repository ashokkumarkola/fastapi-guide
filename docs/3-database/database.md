# DATABASE

SQLModel is built on top of SQLAlchemy and Pydantic

```
PostgreSQL
MySQL
SQLite
Oracle
Microsoft SQL Server, etc.
```

##

```
pip install sqlmodel


```

### Create Models

```
class model_name(SQLModel, table=True):
    instances...

```

### Create an Engine

```
# SQLAlchemy engine
engine = create_engine(db_url, params...)
```

### Create the Tables

```
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
```

### Create a Session Dependency

```
def get_session():
    with Session(engine) as session:
        yield session
```

### Create Database Tables on Startup

@app.on_event("startup")
def on_startup():
create_db_and_tables()
