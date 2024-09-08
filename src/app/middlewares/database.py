from fastapi import Request, Response

from app.ext.db import session_makers


async def database_middleware(request: Request, call_next) -> Response:
    """
    Database Middleware
    :param request: Request
    :param call_next: Any
    :return: Response
    """
    request.state.session_makers = session_makers
    response: Response = await call_next(request)
    return response
