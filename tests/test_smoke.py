def test_app_smoke(client):
    from app import create_app
    app = create_app()
    assert app is not None
    
def test_login_page(client):
    response = client.get('/auth/login')    
    assert response.status_code == 200