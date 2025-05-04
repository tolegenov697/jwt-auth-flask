import json
from app import app, db
import pytest

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
        yield client

def test_register_and_login(client):
    # Регистрация
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'secret'
    })
    assert response.status_code == 201

    # Логин
    response = client.post('/login', json={
        'username': 'testuser',
        'password': 'secret'
    })
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'access_token' in data
