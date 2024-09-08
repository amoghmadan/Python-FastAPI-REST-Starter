import enum

from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app import settings


class Alias(enum.Enum):
    DEFAULT = "default"


engines: dict[str, AsyncEngine] = {
    Alias.DEFAULT.value: create_async_engine(settings.DATABASE_URI),
}

session_makers: dict[str, async_sessionmaker[AsyncSession]] = {
    alias: async_sessionmaker(async_engine, expire_on_commit=False)
    for alias, async_engine in engines.items()
}

Model = type("Model", (AsyncAttrs, DeclarativeBase), {})

__all__ = ["Alias", "Model", "engines", "session_makers"]
