# START, PROD AND DEPLOY

## DEV

```bash
# fastapi alone
fastapi dev main.py

# server
uvicorn main:app --reload
```

---

## ACESS APIs

```bash
# Default
http://127.0.0.1:8000

# Swagger
http://127.0.0.1:8000/docs

# ReDoc
http://127.0.0.1:8000/redoc
```

---

## PROD

```bash
fastapi run main.py

uvicorn main:app --host 0.0.0.0 --port 8000
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
```

---

## DEPLOY

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run server

```bash
fastapi run main.py
uvicorn main:app --host 0.0.0.0 --port 8000

```

###

fastapi login
fastapi deploy

---
