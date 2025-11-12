from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_existing_user():
    r = client.get("/users/1")
    assert r.status_code == 200
    assert r.json()["name"] in {"Alice", "Bob"}


def test_get_missing_user():
    r = client.get("/users/9999")
    assert r.status_code == 404
