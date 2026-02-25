# # from pydantic import BaseSettings
# from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     # model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

#     PROJECT_NAME: str = "My FastAPI Guide"
#     VERSION: str = "1.0.0"
#     ENV: str = "dev"
#     HOST: str = "0.0.0.0"
#     PORT: int = 8000

#     ENVIRONMENT: str = "development"
#     DEBUG: bool = True
#     APP_NAME: str = "FastAPI Guide"
#     SECRET_KEY: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

#     DATABASE_URL: str

#     # Sentry, Redis, etc.
#     SENTRY_DSN: str | None = None

#     model_config = SettingsConfigDict(
#         env_file='.env',
#         extra='ignore'
#     )

#     class Config:
#         env_file = ".env"

# settings = Settings() # type: ignore
