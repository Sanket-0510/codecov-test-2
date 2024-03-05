def test_contact_page(client):
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact Page' in response.data
