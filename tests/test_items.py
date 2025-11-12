from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_items_crud():
    # Стартово порожній список
    r = client.get("/items/")
    assert r.status_code == 200
    assert r.json() == []

    # Створюємо елемент
    payload = {"name": "Phone", "description": "Android"}
    r = client.post("/items/", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] == 1
    assert body["name"] == "Phone"

    # Отримуємо список з 1 елементом
    r = client.get("/items/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1

    # Дістаємо по id
    r = client.get("/items/1")
    assert r.status_code == 200
    assert r.json()["name"] == "Phone"