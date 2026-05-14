# REQUIREMENTS

## Freeze dependencies

```bash
# Generate requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

---

## Language

```
Python
```

---

## IDE

```
VS Code
PyCharm
```

---

## System executable

```bash
sqlite3        # local sql database cli
```

---

## Core Framework

```bash
fastapi        # async api framework, validation, dependency injection, openapi/docs
```

---

## Server

```bash
uvicorn        # asgi server, hot reload, production serving
```

---

## Database

```bash
sqlalchemy     # orm, models, queries, db abstraction
asyncpg        # async postgres driver
alembic        # schema migrations, versioning
```

---

## Authentication / Security

```bash
python-jose    # jwt, jws, token signing/verification
passlib        # password hashing abstraction
bcrypt         # password hashing algorithm
pyjwt          # jwt encode/decode
pwdlib[argon2] # argon2 password hashing
```

---

## Validation / Settings

```bash
pydantic           # validation, serialization, parsing, typed schemas
pydantic-settings  # typed config/envs, validation, parsing, centralized settings, .env support
python-dotenv      # .env loading, env management
```

---

## Utilities

```bash
python-multipart   # form-data, file uploads
email-validator    # email syntax/domain validation
```

---

## Development / Testing

```bash
pytest             # testing framework, assertions, fixtures
httpx              # async/sync http client, api testing
```

---

## API Testing Tools

```text
Postman    # api testing, collections, automation
Swagger    # openapi ui, api docs/testing
Insomnia   # api client/testing
```

---

## Database Tools

```text
PostgreSQL   # production relational database
SQLite       # embedded local database
```

---

## FastAPI Docs Access

```bash
/docs        # swagger ui
/redoc       # redoc documentation ui
```

---
