import asyncio

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

from app_config import PG_DSN


engine = create_async_engine(PG_DSN, echo=True)

async def test_connection():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(res.fetchall())


if __name__ == '__main__':
    asyncio.run(test_connection())