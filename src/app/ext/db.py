from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app import settings

metadata = MetaData()

engines: dict[str, AsyncEngine] = {
    alias: create_async_engine(uri) for alias, uri in settings.DATABASES.items()
}

sessionmakers: dict[str, async_sessionmaker[AsyncSession]] = {
    alias: async_sessionmaker(async_engine, expire_on_commit=False)
    for alias, async_engine in engines.items()
}

Model = type("Model", (AsyncAttrs, DeclarativeBase), {})

__all__ = ["Model", "engines", "metadata", "sessionmakers"]
