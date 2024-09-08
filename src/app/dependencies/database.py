from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession


def get_db(request: Request) -> AsyncSession:
    """
    Use "fastapi.Depends" class and pass this function to access default DB object.
    :param request: Request
    :return: AsyncSession
    """
    return request.state.db
