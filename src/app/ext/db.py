from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app import settings

engines: dict[str, AsyncEngine] = {
    alias: create_async_engine(uri) for alias, uri in settings.DATABASES.items()
}

session_makers: dict[str, async_sessionmaker[AsyncSession]] = {
    alias: async_sessionmaker(async_engine, expire_on_commit=False)
    for alias, async_engine in engines.items()
}

Model = type("Model", (AsyncAttrs, DeclarativeBase), {})

__all__ = ["Model", "engines", "session_makers"]
