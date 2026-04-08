from fastapi import FastAPI
from fastapi.testclient import TestClient
# from starlette.testclient import TestClient

from app.main import test_app

# pytest

app = test_app() # await
client = TestClient(app)

# def | async def
# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Welcome to MyFastAPIApp"}

def test_read_main():
    response = client.get("/")
    data = response.json()

    assert response.status_code == 200
    assert data["message"] == "Welcome to MyFastAPIApp"
    assert "version" in data
    assert "docs" in data
    assert "environment" in data