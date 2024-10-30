import asyncio

from sqlalchemy import Integer
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import text

from app_config import PG_DSN


engine = create_async_engine(PG_DSN, echo=True)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'


async def test_connection():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(res.fetchall())


if __name__ == '__main__':
    asyncio.run(test_connection())