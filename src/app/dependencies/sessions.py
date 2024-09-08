from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def aliased_get_session(alias: str):
    def get_session(request: Request) -> async_sessionmaker[AsyncSession]:
        """
        Use "fastapi.Depends" class and pass this function to access session class.
        :param request: Request
        :return: AsyncSession
        """
        return request.state.session_makers[alias]

    return get_session
