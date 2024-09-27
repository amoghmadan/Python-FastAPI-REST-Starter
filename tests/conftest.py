from typing import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.asgi import get_asgi_application
from app.ext.db import sessionmakers


@pytest.fixture
def app() -> Generator[FastAPI, None, None]:
    """
    Fixture: FastAPI app.
    :return: FastAPI
    """
    app = get_asgi_application()
    app.state.sessionmakers = sessionmakers
    yield app


@pytest.fixture
def client(app) -> Generator[TestClient, None, None]:
    """
    Fixture: Test Client.
    :param app: FastAPI
    :return: TestClient
    """
    with TestClient(app) as client:
        yield client
