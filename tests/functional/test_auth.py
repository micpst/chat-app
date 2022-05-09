import pytest

from app.auth.models import User

@pytest.mark.parametrize('url', ('/signup', '/login'))
def test_get_page(app_client, url):
    """
    Given a Flask application configured for testing
    When the '/signup' or '/login' page is requested (GET)
    Then check that the response is valid
    """
    response = app_client.get(url)
    assert response.status_code == 200


def test_post_signup(app_client, database):
    response = app_client.post('/signup', data={
        'name': 'Michal',
        'email': 'michal.contact@gmail.com',
        'password': 'MyP@$$w0rd'
    }, follow_redirects=True)

    assert len(response.history) == 1
    assert response.request.path == '/chats'
    assert User.query.count() == 1
