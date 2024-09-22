from fastapi import Request, Response
from typing_extensions import Awaitable, Callable


async def database_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """
    Database Middleware
    :param request: Request
    :param call_next: Callable[[Request], Awaitable[Response]]
    :return: Response
    """
    alias: str = "default"
    if alias not in request.app.state.sessionmakers:
        messages = (
            "%r database not configured properly.",
            "Did you forget to specify the %r in the DATABASES settings?",
        )
        raise ValueError(*(msg % alias for msg in messages))

    async with request.app.state.sessionmakers[alias]() as session:
        request.state.db = session
        response: Response = await call_next(request)
    return response
