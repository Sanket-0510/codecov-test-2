

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Page' in response.data
