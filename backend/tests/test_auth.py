import uuid

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def unique_username():
    return f"testuser_{uuid.uuid4().hex[:8]}"


def test_register_user():
    username = unique_username()

    response = client.post(
        "/api/auth/register",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "TestPassword123!",
            "role": "analyst",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == username
    assert data["role"] == "analyst"
    assert data["is_active"] is True
    assert "password" not in data
    assert "password_hash" not in data


def test_duplicate_registration():
    username = unique_username()
    email = f"{username}@example.com"

    payload = {
        "username": username,
        "email": email,
        "password": "TestPassword123!",
        "role": "analyst",
    }

    first_response = client.post(
        "/api/auth/register",
        json=payload,
    )

    assert first_response.status_code == 201

    second_response = client.post(
        "/api/auth/register",
        json=payload,
    )

    assert second_response.status_code == 409


def test_login_success():
    username = unique_username()

    register_response = client.post(
        "/api/auth/register",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "TestPassword123!",
            "role": "analyst",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={
            "username": username,
            "password": "TestPassword123!",
        },
    )

    assert login_response.status_code == 200

    data = login_response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():
    username = unique_username()

    register_response = client.post(
        "/api/auth/register",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "TestPassword123!",
            "role": "analyst",
        },
    )

    assert register_response.status_code == 201

    response = client.post(
        "/api/auth/login",
        json={
            "username": username,
            "password": "WrongPassword123!",
        },
    )

    assert response.status_code == 401


def test_me_with_valid_token():
    username = unique_username()

    register_response = client.post(
        "/api/auth/register",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "TestPassword123!",
            "role": "analyst",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={
            "username": username,
            "password": "TestPassword123!",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.get(
        "/api/auth/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == username
    assert data["role"] == "analyst"


def test_me_without_token():
    response = client.get("/api/auth/me")

    assert response.status_code == 401


def test_me_with_invalid_token():
    response = client.get(
        "/api/auth/me",
        headers={
            "Authorization": "Bearer invalid-token",
        },
    )

    assert response.status_code == 401


def test_users_requires_authentication():
    response = client.get("/api/users")

    assert response.status_code == 401


def test_admin_can_create_user():
    admin_username = unique_username()

    register_response = client.post(
        "/api/auth/register",
        json={
            "username": admin_username,
            "email": f"{admin_username}@example.com",
            "password": "AdminPassword123!",
            "role": "admin",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={
            "username": admin_username,
            "password": "AdminPassword123!",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    new_username = unique_username()

    response = client.post(
        "/api/users",
        params={
            "username": new_username,
            "email": f"{new_username}@example.com",
            "password": "NewUserPassword123!",
            "role": "analyst",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == new_username
    assert data["role"] == "analyst"
    assert "password_hash" not in data


def test_analyst_cannot_create_user():
    username = unique_username()

    register_response = client.post(
        "/api/auth/register",
        json={
            "username": username,
            "email": f"{username}@example.com",
            "password": "AnalystPassword123!",
            "role": "analyst",
        },
    )

    assert register_response.status_code == 201

    login_response = client.post(
        "/api/auth/login",
        json={
            "username": username,
            "password": "AnalystPassword123!",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    new_username = unique_username()

    response = client.post(
        "/api/users",
        params={
            "username": new_username,
            "email": f"{new_username}@example.com",
            "password": "NewUserPassword123!",
            "role": "analyst",
        },
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 403
