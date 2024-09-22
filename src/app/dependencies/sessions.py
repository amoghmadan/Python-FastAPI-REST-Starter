from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class AliasedSessionMaker:
    """Aliased: Session Maker"""

    def __init__(self: "AliasedSessionMaker", alias: str) -> None:
        """
        Set alias to be used as key for getting the async session maker.
        :param alias: str
        """
        self._alias = alias

    def __repr__(self: "AliasedSessionMaker") -> str:
        """
        Representation of class' instance.
        :return: str
        """
        return "<%s %r>" % (self.__class__.__name__, self._alias)

    def __call__(
        self: "AliasedSessionMaker", request: Request
    ) -> async_sessionmaker[AsyncSession]:
        """
        Use "fastapi.Depends" class and pass this object to access session maker class.
        :param request: Request
        :return: async_sessionmaker[AsyncSession]
        """
        if self._alias not in request.app.state.sessionmakers:
            messages = (
                "%r database not configured properly.",
                "Did you forget to specify the %r in the DATABASES settings?",
            )
            raise ValueError(*(msg % self._alias for msg in messages))

        return request.app.state.sessionmakers[self._alias]
