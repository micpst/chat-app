import pytest


@pytest.mark.usefixtures('db_users')
@pytest.mark.parametrize('email, password, num_responses, path, message', (
    pytest.param('t@email.com', 'P@$$w0rd', 0, '/login', b'Invalid email or password.', id='invalid_email'),
    pytest.param('test_1@email.com', 'pass', 0, '/login', b'Invalid email or password.',id='invalid_password'),
    pytest.param('test_1@email.com', 'P@$$w0rd', 1, '/chats', b'', id='valid_email_and_password'),
))
def test_post_login(app_client, email, password, num_responses, path, message):
    """
    Given a Flask application configured for testing and user credentials
    When the '/login' path is requested (POST) and user is not authenticated
    Then check that the response is valid
    """
    response = app_client.post('/login', data={
        'email': email,
        'password': password
    }, follow_redirects=True)

    assert len(response.history) == num_responses
    assert response.request.path == path
    assert message in response.data


@pytest.mark.usefixtures('db_users')
@pytest.mark.parametrize('name, email, password, num_responses, path, message', (
    pytest.param('', 'test_1@email.com', 'P@$$w0rd', 0, '/signup', b'', id='invalid_name'),
    pytest.param('test', '', 'P@$$w0rd', 0, '/signup', b'', id='invalid_email'),
    pytest.param('test', 'test_1@email.com', '', 0, '/signup', b'', id='invalid_password'),
    pytest.param('test', 'test_1@email.com', 'P@$$w0rd', 0, '/signup', b'User already exists.', id='duplicated_email'),
    pytest.param('test', 'test_3@email.com', 'P@$$w0rd', 1, '/chats', b'', id='valid_name_email_and_password'),
))
def test_post_signup(app_client, name, email, password, num_responses, path, message):
    """
    Given a Flask application configured for testing and user credentials
    When the '/signup' path is requested (POST) and user is not authenticated
    Then check that the response is valid
    """
    response = app_client.post('/signup', data={
        'name': name,
        'email': email,
        'password': password
    }, follow_redirects=True)

    assert len(response.history) == num_responses
    assert response.request.path == path
    assert message in response.data


@pytest.mark.usefixtures('login_user')
def test_get_logout(app_client):
    """
    Given a Flask application configured for testing
    When the '/logout' path is requested (GET) and user is authenticated
    Then check that the response is valid
    """
    response = app_client.get('/logout', follow_redirects=True)

    assert len(response.history) == 1
    assert response.request.path == '/login'
    assert b'You were logged out.' in response.data
