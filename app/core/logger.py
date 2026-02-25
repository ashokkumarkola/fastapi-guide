import logging
# import logging.config
# from logging.handlers import RotatingFileHandler
# from pathlib import Path

# LOG_DIR = Path("logs")
# LOG_DIR.mkdir(exist_ok=True)

# LOG_FILE = LOG_DIR / "app.log"


# ======================== Approach 1 Logger ======================== #
# Function-based logger | Manual Python configuration.

def setup_logger():

    # ---- Disable uvicorn logs ----
    # logging.getLogger("uvicorn").handlers = []
    # logging.getLogger("uvicorn.error").handlers = []
    # logging.getLogger("uvicorn.access").handlers = []

    # logging.getLogger("uvicorn").propagate = False
    # logging.getLogger("uvicorn.error").propagate = False
    # logging.getLogger("uvicorn.access").propagate = False

    # ---- app logger ----
    logger = logging.getLogger("app") # Named Logger
    # logger.setLevel(logging.INFO) # Set Log Level

    # Stop logger
        # Development → INFO
        # Production  → WARNING / ERROR
        # Testing     → OFF > CRITICAL
    logger.setLevel(logging.CRITICAL + 1)

    # Prevent duplicate logs | FastAPI reload runs app twice.
    if logger.handlers:
        return logger

    # ---------- FORMAT ----------
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    # ---------- CONSOLE HANDLER ----------
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # ---------- FILE HANDLER ----------
    # file_handler = RotatingFileHandler(
    #     LOG_FILE,
    #     maxBytes=5 * 1024 * 1024,  # 5MB
    #     backupCount=3
    # )
    # file_handler.setFormatter(formatter)

    # ---------- CLOUD HANDLER ----------

    # ---------- DATABASE HANDLER ----------

    # ---------- ADD HANDLERS ----------
    logger.addHandler(console_handler)
    # logger.addHandler(file_handler)

    return logger

# Export Logger | Runs automatically when imported.
logger = setup_logger()

# ======================== Approach 2 Logger ======================== #
# Configuration-driven logging (dictConfig) | standard logging system.

# LOGGING_CONFIG = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "default": {
#             "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#             "formatter": "default",
#         },
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "logs/app.log",
#             "formatter": "default",
#         },
#     },
#     "root": {
#         "handlers": ["console", "file"],
#         "level": "INFO",
#     },
# }

# logging.config.dictConfig(LOGGING_CONFIG)

# logger = logging.getLogger("app")


# ======================== Simple Logger ======================== #
# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# Logging Levels
    # debug()	developer debugging
    # info()	normal events
    # warning()	unexpected but ok
    # error()	failure occurred
    # critical()	system crash

# logging.yaml
# logging.json
# env-based configs
