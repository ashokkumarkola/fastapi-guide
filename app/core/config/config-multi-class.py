# Multi class config 

from enum import Enum
from typing import List
from functools import lru_cache
from pydantic import Field, PostgresDsn, AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# =========================================================
# ENVIRONMENT TYPES
# =========================================================

class Environment(str, Enum):
    LOCAL = "local"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"


# =========================================================
# APP SETTINGS
# =========================================================

class AppSettings(BaseSettings):
    app_name: str = "Ecommerce Backend"
    app_version: str = "1.0.0"
    environment: Environment = Environment.LOCAL
    debug: bool = True
    api_v1_prefix: str = "/api/v1"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    # Environment Helpers
    @property
    def is_local(self) -> bool:
        return self.environment == Environment.LOCAL

    @property
    def is_test(self) -> bool:
        return self.environment == Environment.TEST

    @property
    def is_staging(self) -> bool:
        return self.environment == Environment.STAGING

    @property
    def is_production(self) -> bool:
        return self.environment == Environment.PRODUCTION


# =========================================================
# DATABASE SETTINGS
# =========================================================

class DatabaseSettings(BaseSettings):
    # url: str = Field(..., alias="DATABASE_URL")
    url: PostgresDsn = Field(..., alias="DATABASE_URL")

    echo: bool = False
    pool_size: int = 10
    max_overflow: int = 20
    pool_timeout: int = 30
    pool_recycle: int = 1800
    pool_pre_ping: bool = True


# =========================================================
# SECURITY SETTINGS
# =========================================================

class SecuritySettings(BaseSettings):
    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7


# =========================================================
# REDIS SETTINGS
# =========================================================

class RedisSettings(BaseSettings):
    url: str = Field(
        default="redis://localhost:6379",
        alias="REDIS_URL"
    )
    cache_ttl: int = 3600


# =========================================================
# LOGGING SETTINGS
# =========================================================

class LoggingSettings(BaseSettings):
    level: str = "INFO"

    format: str = (
        "%(asctime)s | %(levelname)s | "
        "%(name)s | %(message)s"
    )


# =========================================================
# MAIN SETTINGS
# =========================================================

class Settings(BaseSettings):

    app: AppSettings = AppSettings()

    database: DatabaseSettings = DatabaseSettings()

    security: SecuritySettings = SecuritySettings()

    redis: RedisSettings = RedisSettings()

    logging: LoggingSettings = LoggingSettings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


# =========================================================
# SETTINGS SINGLETON
# =========================================================

@lru_cache
def get_settings() -> Settings:
    """
    Returns cached settings instance.
    Prevents reloading environment repeatedly.
    """
    return Settings()


settings = get_settings()


# ======== USAGE ======== #
# from app.core.config import get_settings
# settings = get_settings()
# VARABLE = settings.section.VARIABLE