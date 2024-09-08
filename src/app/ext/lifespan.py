from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.ext.db import session_makers


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.session_makers = session_makers
    yield
