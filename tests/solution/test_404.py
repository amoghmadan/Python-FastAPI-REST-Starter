from http import HTTPStatus
from random import randint

from fastapi.testclient import TestClient

url = "/" + "".join([chr(randint(97, 122)) for _ in range(10)])


def test_http_404(client: TestClient) -> None:
    """Test: HTTP 404"""
    response = client.get(url)
    assert response.status_code == HTTPStatus.NOT_FOUND
