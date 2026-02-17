from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from app.db.async_db.async_config import Config

engine = AsyncEngine(
    create_engine(
    url = Config.ASYNC_DB_URL,
    echo = True
))

async def init_db():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")

        result = await conn.execute(statement)

        print(result.all())


