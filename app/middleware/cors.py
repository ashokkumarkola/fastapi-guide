import os
from app.core.config import get_settings
from fastapi.middleware.cors import CORSMiddleware

settings = get_settings()

# ============================================================
# Setup CORS Middleware
# ============================================================

def get_allowed_origins() -> list:
    """
    Reads allowed origins from an environment variable.
    Expects a comma-separated string. Provides secure defaults.
    """
    origins_str = settings.ALLOWED_ORIGINS # os.getenv("ALLOWED_ORIGINS", "")
    if origins_str:
        # Split the comma-separated string into a list and strip whitespace
        return [origin.strip() for origin in origins_str.split(",")]
    else:
        # In production, if the env var is not set, return an empty list
        # to block all cross-origin requests by default (safe default).
        # For development, you might allow a localhost default.
        if os.getenv("ENVIRONMENT") == "development":
            return ["http://localhost:3000", "http://127.0.0.1:3000"]
        return []

def setup_cors(app):
    """
    Attach CORS middleware to FastAPI application.

    This function keeps main.py clean and allows
    centralized middleware configuration.
    """

    allowed_origins = [

        # Frontend development servers
        "http://localhost:3000",
        "http://127.0.0.1:3000",

        # Example production domains
        # "https://myapp.com",
        # "https://admin.myapp.com",
    ]

    app.add_middleware(
        CORSMiddleware,

        # Allowed origins
        allow_origins=allowed_origins, # get_allowed_origins()

        # Allow cookies and authentication headers
        allow_credentials=True,

        # Allowed HTTP methods
        allow_methods=[
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
            "OPTIONS",
        ],

        # Allowed request headers
        allow_headers=[
            "Authorization",
            "Content-Type",
            "Accept",
            "Origin",
            "User-Agent",
        ],

        # Headers exposed to frontend
        expose_headers=[
            "Content-Length",
            "Content-Type",
        ],

        # Cache preflight response (seconds)
        max_age=3600,
    )

def dynamic_origin_validator(origin: str) -> bool:
    """
    Optional: More complex logic, e.g., checking against a database or regex.
    This function would be called by `allow_origin_regex` or a custom solution.
    """
    # Example: Allow any subdomain of myapp.com
    # if origin and origin.endswith(".myapp.com"):
    #     return True
    # return False
    pass
