from fastapi import Request, Response

from app.ext.db import session_makers


async def database_middleware(request: Request, call_next) -> Response:
    """
    Database Middleware
    :param request: Request
    :param call_next: Any
    :return: Response
    """
    async with session_makers["default"]() as session:
        request.state.db = session
        response: Response = await call_next(request)
    return response
