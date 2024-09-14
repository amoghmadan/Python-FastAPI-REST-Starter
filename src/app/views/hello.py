from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.schemas.domain.hello import World


async def world(db: AsyncSession = Depends(get_db)) -> World:
    """Hello, world from DB."""
    stmt = text("SELECT 'World!' AS world;")
    result = await db.execute(stmt)
    first = result.scalar_one()
    return World(hello=first)
