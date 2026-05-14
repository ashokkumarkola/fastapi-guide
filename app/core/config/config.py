# Single class config
from enum import Enum
from typing import List
from functools import lru_cache
from pydantic import Field, PostgresDsn, AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Environment Enum
class Environment(str, Enum):
    LOCAL = "local"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"

class Settings(BaseSettings):
    """Application settings with environment variable support"""

    # ======== APP SETTINGS ========
    APP_NAME: str = "My FastAPI Guide"
    APP_VERSION: str = "1.0.0"

    # Environment
    ENVIRONMENT: str = Environment.LOCAL
    DEBUG: bool = True

    API_V1_PREFIX: str = "/api/v1" # API_V1_STR

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    # Docs
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/openapi.json"


    # ======== SECURITY ========
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


    # ======== CORS ========
    # BACKEND_CORS_ORIGINS: List[str] = []
    ALLOWED_ORIGINS: list[AnyHttpUrl] = []
    

    # ======== DATABASE ========
    # DATABASE_URL: str
    DATABASE_URL: PostgresDsn
    ECHO: bool = False
    POOL_SIZE: int = 10
    MAX_OVERFLOW: int = 20
    POOL_TIMEOUT: int = 30
    POOL_RECYCLE: int = 1800
    POOL_PRE_PING: bool = True


    # ======== FILE UPLOADS ========
    BASE_UPLOAD_DIR: str = "uploads"


    # ======== REDIS ========
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_TTL: int = 3600


    # ======== LOGGING ========
    # LOGS: bool = True
    LOG_LEVEL: str = "INFO"
    FORMATTER: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Sentry, Redis, etc.
    # SENTRY_DSN: str | None = None
    # REDIS_URL: str = "redis://localhost:6379/0"


    # ======== Validators ========
    @field_validator("SECRET_KEY", mode="before")
    def validate_secret_key(cls, v):
        if not v or len(v) < 32:
            raise ValueError("SECRET_KEY must be at least 32 characters")
        return v
    
    # @field_validator("ALLOWED_ORIGINS", mode="before")
    # def assemble_cors_origins(cls, v):
    #     if isinstance(v, str):
    #         return [i.strip() for i in v.split(",")]
    #     return v
    
    # ======== Configuring models ========
    # Pydantic v1
    # class Config:
    #     env_file = ".env"
    #     case_sensitive = True

    # Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        # env_ignore_empty=True, 
        extra="ignore"
    )

# settings = Settings() # type: ignore

@lru_cache()
def get_settings() -> Settings:
    """Cached settings to avoid reading .env file repeatedly"""
    return Settings()

settings = get_settings()

# ======== USAGE ======== #
# from app.core.config import get_settings
# settings = get_settings()
# VARABLE = settings.VARIABLE


# ======== DEBUG ======== #
# Declared in Settings but NOT in .env
