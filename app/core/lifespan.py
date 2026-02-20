from fastapi import FastAPI
from contextlib import contextmanager, asynccontextmanager
from app.db.session import init_db #, connect
from app.core.logger import logger

# --------------- ASYNC ---------------
@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup
    # app.state.db = connect()
    # print("DB connected")

    logger.info("# ======== Application Started ======== #")
    init_db()
    logger.info("DB Initialized.")
    

    yield

    # shutdown
    # app.state.db.close()
    # print("DB closed")

    logger.info("# ======== Application shutdown ======== #")
    

# --------------- SYNC ---------------
# @contextmanager
# def lifespan(app: FastAPI):

#     app.state.db = connect()
#     print("DB connected")

#     yield

#     app.state.db.close()
#     print("DB closed")
