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
    assert json_data['application'] == "Student Grade Calculator"

def test_health_route(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == "healthy"

def test_calculate_route_valid(client):
    response = client.get('/calculate?marks=80,90,70')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['total'] == 240.0
    assert json_data['average'] == 80.0

def test_calculate_route_invalid(client):
    response = client.get('/calculate?marks=abc,90')
    assert response.status_code == 400
    
    response_empty = client.get('/calculate')
    assert response_empty.status_code == 400
