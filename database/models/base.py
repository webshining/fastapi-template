from sqlalchemy import select
from sqlalchemy.ext.asyncio import (AsyncAttrs, AsyncSession,
                                    async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase

from core.config import DATABASE_URI

async_engine = create_async_engine(DATABASE_URI)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class BaseModel(Base):
    __abstract__ = True

    @classmethod
    async def get(cls, session: AsyncSession, id: int):
        stmt = select(cls).where(cls.id == id)
        obj = await session.scalar(stmt)
        session.expunge_all()
        return obj

    @classmethod
    async def create(cls, session: AsyncSession, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        await session.flush()
        session.expunge_all()
        return obj


async def get_session() -> AsyncSession:
    async with async_session() as session:
        async with session.begin():
            yield session
