from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from app import settings


@pytest.mark.skipif(not settings.DEBUG, reason="DEBUG is False.")
def test_openapi(client: TestClient) -> None:
    """Test: OpenAPI"""
    url = settings.OPENAPI["openapi_url"]
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


@pytest.mark.skipif(not settings.DEBUG, reason="DEBUG is False.")
def test_swagger(client: TestClient) -> None:
    """Test: Swagger"""
    url = "/docs"
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK
