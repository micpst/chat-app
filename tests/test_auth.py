import pytest


@pytest.mark.usefixtures('db_users')
@pytest.mark.parametrize('email, password, message', (
    pytest.param('t@email.com', 'P@$$w0rd', b'Invalid email or password.', id='invalid_email'),
    pytest.param('test_1@email.com', 'P@ssw0rd', b'Invalid email or password.', id='invalid_password'),
))
def test_post_login_flash_message(app_client, email, password, message):
    response = app_client.post('/login', data={
        'email': email,
        'password': password
    })
    assert message in response.data


@pytest.mark.usefixtures('db_users')
def test_post_signup_flash_message(app_client):
    response = app_client.post('/signup', data={
        'name': 'test_1',
        'email': 'test_1@email.com',
        'password': 'P@$$w0rd'
    })
    assert b'User already exists.' in response.data


@pytest.mark.usefixtures('db_users')
@pytest.mark.parametrize('email, password, num_responses, path', (
    pytest.param('test_1@email.com', 'pass', 0, '/login', id='invalid_email'),
    pytest.param('t@email.com', 'P@$$w0rd', 0, '/login', id='invalid_password'),
    pytest.param('test_1@email.com', 'P@$$w0rd', 1, '/chats', id='valid_email_and_password'),
))
def test_post_login_redirect(app_client, email, password, num_responses, path):
    response = app_client.post('/login', data={
        'email': email,
        'password': password
    }, follow_redirects=True)

    assert len(response.history) == num_responses
    assert response.request.path == path


@pytest.mark.usefixtures('db_users')
@pytest.mark.parametrize('name, email, password, num_responses, path', (
    pytest.param('', 'test_1@email.com', 'P@$$w0rd', 0, '/signup', id='invalid_name'),
    pytest.param('test', '', 'P@$$w0rd', 0, '/signup', id='invalid_email'),
    pytest.param('test', 'test_1@email.com', 'P@$$w0rd', 0, '/signup', id='duplicated_email'),
    pytest.param('test', 'test_1@email.com', '', 0, '/signup', id='invalid_password'),
    pytest.param('test', 'test_3@email.com', 'P@$$w0rd', 1, '/chats', id='valid_name_email_and_password'),
))
def test_post_signup_redirect(app_client, name, email, password, num_responses, path):
    response = app_client.post('/signup', data={
        'name': name,
        'email': email,
        'password': password
    }, follow_redirects=True)

    assert len(response.history) == num_responses
    assert response.request.path == path


@pytest.mark.usefixtures('login_user')
def test_get_logout_redirect(app_client):
    response = app_client.get('/logout', follow_redirects=True)

    assert len(response.history) == 1
    assert response.request.path == '/login'
    assert b'You were logged out.' in response.data
