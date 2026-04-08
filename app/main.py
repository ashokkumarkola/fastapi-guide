# from functools import lru_cache
from app.core.app import create_app
# from app.core.config import get_settings
# from app.core.instrumentation import instrument_app

# settings = get_settings()

# ENV = settings.ENVIRONMENT

# -------- Lazy Initialization (Performance Optimization) --------
# @lru_cache
# def get_application():
#     app = create_app()

#     if settings.ENABLE_TELEMETRY:
#         instrument_app(app)

#     return app

# -------- App --------
# app = get_application()
# app = create_app(env=ENV)
app = create_app()


# -------- Run --------
def run():
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )


# -------- Test --------
def test_app():
    return create_app()


# -------- Main --------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
