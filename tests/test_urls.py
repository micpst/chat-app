import pytest


@pytest.mark.parametrize('path, status_code', (
    pytest.param('/', 302, id='/'),
    pytest.param('/chats', 302, id='/chats'),
    pytest.param('/login', 200, id='/login'),
    pytest.param('/logout', 302, id='/logout'),
    pytest.param('/signup', 200, id='/signup'),
))
def test_get_path_not_authenticated(app_client, path, status_code):
    """
    Given a Flask application configured for testing
    When the path is requested (GET) and user is not authenticated
    Then check that the correct response status code is returned
    """
    response = app_client.get(path)
    assert response.status_code == status_code


@pytest.mark.usefixtures('login_user')
@pytest.mark.parametrize('path, status_code', (
    pytest.param('/', 302, id='/'),
    pytest.param('/chats', 200, id='/chats'),
    pytest.param('/login', 302, id='/login'),
    pytest.param('/logout', 302, id='/logout'),
    pytest.param('/signup', 302, id='/signup'),
))
def test_get_path_authenticated(app_client, path, status_code):
    """
    Given a Flask application configured for testing
    When the path is requested (GET) and user is authenticated
    Then check that the correct response status code is returned
    """
    response = app_client.get(path)
    assert response.status_code == status_code
