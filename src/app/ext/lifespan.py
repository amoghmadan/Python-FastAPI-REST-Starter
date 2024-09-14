from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.applications import AppType, Lifespan

from app.ext.db import session_makers


@asynccontextmanager
async def lifespan(app: FastAPI) -> Lifespan[AppType]:
    """
    Lifespan to load content in application state or perform operations before startup.
    :param app: FastAPI
    :return: Lifespan[AppType]
    """
    app.state.session_makers = session_makers
    yield
