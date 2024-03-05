import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact Page' in response.data
