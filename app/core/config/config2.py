# Multi class config 

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# =========================================================
# APP SETTINGS
# =========================================================

class AppSettings(BaseSettings):
    app_name: str = "Ecommerce Backend"
    environment: str = "local"
    debug: bool = True
    api_v1_prefix: str = "/api/v1"


# =========================================================
# DATABASE SETTINGS
# =========================================================

class DatabaseSettings(BaseSettings):
    url: str = Field(..., alias="DATABASE_URL")

    pool_size: int = 10
    max_overflow: int = 20
    pool_pre_ping: bool = True
    echo: bool = False


# =========================================================
# SECURITY SETTINGS
# =========================================================

class SecuritySettings(BaseSettings):
    secret_key: str = Field(..., alias="SECRET_KEY")

    algorithm: str = "HS256"

    access_token_expire_minutes: int = 30


# =========================================================
# REDIS SETTINGS
# =========================================================

class RedisSettings(BaseSettings):
    url: str = Field(
        default="redis://localhost:6379",
        alias="REDIS_URL"
    )


# =========================================================
# LOGGING SETTINGS
# =========================================================

class LoggingSettings(BaseSettings):
    level: str = "INFO"


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
    return Settings()


settings = get_settings()