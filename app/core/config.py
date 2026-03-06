from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pydantic import validator, field_validator, AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    """Application settings with environment variable support"""

    PROJECT_NAME: str = "My FastAPI Guide"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    # BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ALLOWED_ORIGINS: list[str] = []
    
    # Database
    DATABASE_URL: str
    # ASYNC_DB_URL: str | None = None
    
    # Environment
    ENVIRONMENT: str = "dev"

    # Upload Files
    BASE_UPLOAD_DIR: str = "uploads"

    # Logs
    # LOGS: bool = True

    # Sentry, Redis, etc.
    # SENTRY_DSN: str | None = None
    # REDIS_URL: str = "redis://localhost:6379/0"

    # @field_validator("SECRET_KEY", pre=True)
    # def validate_secret_key(cls, v):
    #     if not v or len(v) < 32:
    #         raise ValueError("SECRET_KEY must be at least 32 characters")
    #     return v
    
    # @field_validator("BACKEND_CORS_ORIGINS", pre=True)
    # def assemble_cors_origins(cls, v):
    #     if isinstance(v, str):
    #         return [i.strip() for i in v.split(",")]
    #     return v
    
    # ---- Configuring models ---- #
    # Pydantic v1
    # class Config:
    #     env_file = ".env"
    #     case_sensitive = True

    # Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        # env_ignore_empty=True, 
        # extra="ignore"
    )

# settings = Settings() # type: ignore

@lru_cache()
def get_settings():
    """Cached settings to avoid reading .env file repeatedly"""
    return Settings()

# Declared in Settings but NOT in .env

# ======== USAGE ======== #
# from app.core.config import get_settings
# settings = get_settings()
# VARABLE = settings.VARIABLE
