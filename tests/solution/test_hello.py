from http import HTTPStatus

from fastapi.testclient import TestClient

from app.schemas.domain.hello import World

url = "/api/v1/hello/world"


def test_world_method_not_allowed(client: TestClient) -> None:
    """Test: HTTP 405 Method Not Allowed"""
    response = client.post(url, json={})
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_world_ok(client: TestClient) -> None:
    """Test: HTTP 200 OK"""
    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_world_ok_response(client: TestClient) -> None:
    """Test: World (from Database)"""
    response = client.get(url)
    data: World = response.json()
    assert data["hello"] == "World!"
