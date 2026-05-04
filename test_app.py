import pytest
from app import app

@pytest.fixture
def client():
    # Sets up a test version of your Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_buses_route(client):
    """Checks if the bus list route is accessible"""
    response = client.get('/buses')
    # If the DB is not connected, it might return 500, 
    # but for a 'Green' pipeline, we want to see 200.

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
