import uuid
import pytest
import requests
from api.endpoints.endpoints import Url, Endpoints


@pytest.fixture
def new_user():
    name = "testUser"
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    password = "P@ssw0rd!"

    resp = requests.post(
        f"{Url.BASE_URL}{Endpoints.REGISTER_USER}",
        json={"email": email, "password": password, "name": name},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["success"] is True
    return {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": data["accessToken"],
        "refreshToken": data["refreshToken"]
    }

@pytest.fixture
def auth_tokens(new_user):
    # логинимся тем же пользователем
    resp = requests.post(
        f"{Url.BASE_URL}{Endpoints.AUTH_USER}",
        json={"email": new_user["email"], "password": new_user["password"]},
    )

    assert resp.status_code == 200, f"Login failed: {resp.status_code}, {resp.text[:100]}"
    tokens = resp.json()
    return tokens
