from http import HTTPMethod, HTTPStatus

from fastapi import APIRouter

from app.views.hello import world

hello = APIRouter(prefix="/hello")
hello.add_api_route(
    "/world", world, methods=[HTTPMethod.GET], status_code=HTTPStatus.OK
)
