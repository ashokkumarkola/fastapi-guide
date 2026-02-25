from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    """Application settings with environment variable support"""
    PROJECT_NAME: str = "My FastAPI Guide"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "sqlite:///./fastapi_guide.db"
    ASYNC_DB_URL: str | None = None
    
    # Security
    SECRET_KEY: str = "fastapi-guide-by-ashoka"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Environment
    ENVIRONMENT: str = "development"
    
    # ---- Configuring models ---- #
    # Pydantic v1
    # class Config:
    #     env_file = ".env"
    #     case_sensitive = True

    # Pydantic v2
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

@lru_cache()
def get_settings():
    """Cached settings to avoid reading .env file repeatedly"""
    return Settings()
