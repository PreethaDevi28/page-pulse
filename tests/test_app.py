import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_invalid_request(client):
    response = client.post(
        "/audit",
        json={"url": ""}
    )

    # Empty URL should return 400
    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data
    assert data["error"] == "Please enter a URL"