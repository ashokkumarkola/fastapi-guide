# Start, Run & Deploy

> FastAPI Runtime Commands

---

## Development Server

```bash
# FastAPI CLI
fastapi dev app/main.py

# Uvicorn
uvicorn app.main:app --reload

# Using uv
uv run uvicorn app.main:app --reload
```

---

## Development Flags

```bash
# Auto Reload
--reload

# Custom Host
--host 0.0.0.0

# Custom Port
--port 8000

# Combined
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Access APIs

```bash
# Root
http://127.0.0.1:8000

# Swagger UI
http://127.0.0.1:8000/docs

# ReDoc
http://127.0.0.1:8000/redoc

# OpenAPI Schema
http://127.0.0.1:8000/openapi.json
```

---

## Production Run

> Never use `--reload` in production

```bash
# FastAPI CLI
fastapi run app/main.py

# Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Multiple Workers
uvicorn app.main:app --workers 4 --host 0.0.0.0 --port 8000
```

---

## Gunicorn + Uvicorn Workers

> Common Linux production setup

### Install

```bash
pip install gunicorn
```

### Run

```bash
gunicorn app.main:app -k uvicorn.workers.UvicornWorker -w 4
```

---

## Install Dependencies

```bash
# pip
pip install -r requirements.txt

# uv
uv sync

# Poetry
poetry install
```

---

## Environment Variables

```powershell
# Linux / macOS
export ENV=production

# Windows
set ENV=production
```

---

## Common Production Stack

```text
FastAPI
→ Uvicorn
→ Gunicorn
→ Nginx
→ Docker
→ Linux VPS
```

---

## Reverse Proxy

### Nginx Responsibilities

- SSL
- HTTPS
- Load balancing
- Static files
- Reverse proxy

---

## Docker Run

```bash
# Build Image
docker build -t fastapi-app .

# Run Container
docker run -p 8000:8000 fastapi-app
```

---

## Docker Compose

```bash
# Start Services
docker compose up

# Detached Mode
docker compose up -d

# Stop Services
docker compose down
```

---

## Production Checklist

### Required

- HTTPS
- Environment variables
- Logging
- Monitoring
- Backups
- CORS config
- Rate limiting
- Health checks

---

## Health Check Endpoint

### Example

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

---

## Process Management

### systemd

```bash
sudo systemctl start myapp
sudo systemctl restart myapp
sudo systemctl status myapp
```

---

## Logs

```bash
# Docker Logs
docker logs <container_id>

# Linux Logs
journalctl -u myapp
```

---

## Important Notes

### Dev

```text
Use --reload
Single worker
Debug friendly
```

### Production

```text
No --reload
Multiple workers
Reverse proxy
HTTPS enabled
```

---

## FastAPI Cloud Deploy

### Login

```bash
fastapi login
```

### Deploy

```bash
fastapi deploy
```

---

## Most Used Commands

```bash
# Dev
uv run uvicorn app.main:app --reload

# Production
uvicorn app.main:app --workers 4 --host 0.0.0.0 --port 8000

# Docker
docker compose up -d

# Gunicorn
gunicorn app.main:app -k uvicorn.workers.UvicornWorker -w 4
```

<!-- # START, PROD AND DEPLOY

## DEV

```bash
# fastapi alone
fastapi dev app.main.py

# uvicorn server
uvicorn app.main:app --reload

# uv
uv run uvicorn app.main:app --reload
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

uvicorn app.main:app --host 0.0.0.0 --port 8000
uvicorn app.main:app --workers 4 --host 0.0.0.0 --port 8000
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
uv run uvicorn app.main:app --reload

```

###

```
fastapi login
fastapi deploy
```

--- -->
