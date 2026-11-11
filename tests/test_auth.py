def test_register_user(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "full_name": "Kevin Teste",
            "email": "kevin@test.com",
            "password": "secretpassword123",
            "role": "admin"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "kevin@test.com"
    assert "id" in data

def test_login_user(client):
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "kevin@test.com",
            "password": "secretpassword123"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data
    assert data["token_type"] == "bearer"

def test_unauthorized_access(client):
    response = client.get("/api/v1/users/me")
    assert response.status_code == 401