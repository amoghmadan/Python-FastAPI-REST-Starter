import logging
import logging.config
from http import HTTPStatus

from fastapi import Request, Response
from fastapi.responses import JSONResponse


async def exception_middleware(request: Request, call_next) -> Response:
    """
    Exception Middleware
    :param request: Request
    :param call_next: Any
    :return: Response
    """
    response = JSONResponse(
        {"detail": HTTPStatus.INTERNAL_SERVER_ERROR.phrase},
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
    )
    try:
        response = await call_next(request)
    except Exception as e:
        logging.error(e, exc_info=True)
    return response
