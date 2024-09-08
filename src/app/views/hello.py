from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.dependencies import aliased_get_session
from app.ext.db import Alias


async def world(
    default_session: async_sessionmaker[AsyncSession] = Depends(
        aliased_get_session(Alias.DEFAULT.value)
    ),
) -> dict[str, str]:
    """Hello, world from DB."""
    stmt = text("SELECT 'World!' AS world;")
    async with default_session() as db:
        result = await db.execute(stmt)
        row = result.fetchone()
    return {"hello": row[0]}
