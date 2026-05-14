# CONFIG

Different approaches to write config in projects.

---

# Single File Config

Simple beginner approach.

```python id="9l9mzc"
# config.py

DEBUG = True
DB_HOST = "localhost"
DB_PORT = 5432
SECRET_KEY = "secret"
```

Usage:

```python id="9yy0d8"
from config import DEBUG
```

---

# Class Based Config

Clean and scalable.

```python id="93yygu"
class Config:
    DEBUG = True
    DB_HOST = "localhost"
    DB_PORT = 5432
```

Usage:

```python id="xyit0i"
from config import Config

print(Config.DB_HOST)
```

---

# Environment Based Config

Production standard.

```python id="q8q2f3"
import os

DB_HOST = os.getenv("DB_HOST")
SECRET_KEY = os.getenv("SECRET_KEY")
```

`.env`

```env id="0l5h8s"
DB_HOST=localhost
SECRET_KEY=mysecret
```

---

# Pydantic Settings (Best Modern Approach)

Typed + validated config.

```python id="q7ybkq"
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    db_host: str

    class Config:
        env_file = ".env"

settings = Settings()
```

Usage:

```python id="jlwmqw"
print(settings.db_host)
```

---

# YAML Config

Useful for large structured configs.

`config.yaml`

```yaml id="69vlm4"
app:
  name: MyApp
  debug: true

database:
  host: localhost
  port: 5432
```

Read YAML:

```python id="k8ztkh"
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

print(config["database"]["host"])
```

---

# JSON Config

Simple structured config.

`config.json`

```json id="4u7rxq"
{
  "debug": true,
  "db_host": "localhost"
}
```

Read:

```python id="1j3k0l"
import json

with open("config.json") as f:
    config = json.load(f)
```

---

# Singleton Settings Object

Most common modern backend pattern.

```text id="3jprc6"
.env
 ↓
Pydantic Settings
 ↓
Validated typed config
 ↓
Singleton settings object
 ↓
Used across entire app
```

Example:

```python id="u54lqv"
# settings.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

Anywhere:

```python id="8y2s36"
from settings import settings

print(settings.db_url)
```

---

# Cached Config

Avoid reloading repeatedly.

```python id="5gh9dr"
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyApp"

@lru_cache
def get_settings():
    return Settings()
```

Usage:

```python id="zt4feh"
settings = get_settings()
```

---

## USAGE

```bash
from app.core.config import get_settings
settings = get_settings()
VARABLE = settings.VARIABLE
```

---

## Production Evolution Path

```text id="dh2dyo"
Docker env vars
 ↓
Kubernetes secrets
 ↓
AWS Secrets Manager
 ↓
Vault
 ↓
CI/CD injected secrets
```

---

# Real Project Recommendation

| Project Size    | Best Approach         |
| --------------- | --------------------- |
| Small scripts   | single file           |
| Medium apps     | class config          |
| Backend APIs    | Pydantic settings     |
| Enterprise apps | env + secrets manager |
| DevOps/cloud    | Kubernetes secrets    |

---

# Best Practice

✅ keep secrets in `.env`
✅ never hardcode passwords
✅ use typed config
✅ use singleton settings
✅ validate config at startup
✅ add `.env` to `.gitignore`

`.gitignore`

```gitignore id="i0r4yf"
.env
```
