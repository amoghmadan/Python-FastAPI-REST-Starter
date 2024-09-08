from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db


async def world(db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    """Hello, world from DB."""
    stmt = text("SELECT 'World!' AS world;")
    result = await db.execute(stmt)
    row = result.fetchone()
    return {"hello": row[0]}
