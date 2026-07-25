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
    import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# Happy Path
def test_valid_request(client):
    response = client.post(
        "/audit",
        json={"url": "https://example.com"}
    )

    assert response.status_code == 200
    data = response.get_json()
    assert "status" in data


# Failure Case 1
def test_empty_url(client):
    response = client.post(
        "/audit",
        json={"url": ""}
    )

    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


# Failure Case 2
def test_missing_url_field(client):
    response = client.post(
        "/audit",
        json={}
    )

    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data