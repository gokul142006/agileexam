import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['version'] == "2.0.0"

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_calculate_grade_a(client):
    response = client.get('/calculate?marks=95,90,92')
    json_data = response.get_json()
    assert json_data['grade'] == "A"

def test_calculate_grade_f(client):
    response = client.get('/calculate?marks=50,40,30')
    json_data = response.get_json()
    assert json_data['grade'] == "F"
