import pytest

from app import create_app, db as _db, socketio
from app.auth.models import User
from app.chat.models import Message


@pytest.fixture(scope='function')
def app():
    app = create_app('testing')
    with app.app_context():
        _db.create_all()
        yield app
        _db.session.close()
        _db.drop_all()


@pytest.fixture(scope='function')
def app_client(app):
    with app.test_client() as client:
        yield client


@pytest.fixture(scope='function')
def sio_client(app, app_client):
    return socketio.test_client(app, flask_test_client=app_client)


@pytest.fixture(scope='function')
def db(app):
    return _db


@pytest.fixture(scope='function')
def db_users(db):
    db.session.add(User('test_1', 'test_1@email.com', 'P@$$w0rd'))
    db.session.add(User('test_2', 'test_2@email.com', 'P@$$w0rd'))
    db.session.commit()


@pytest.fixture(scope='function')
def db_messages(db):
    db.session.add(Message('msg_1_2', 1, 2))
    db.session.add(Message('msg_2_1', 2, 1))
    db.session.commit()


@pytest.fixture(scope='function')
def login_user(app_client, db_users):
    app_client.post('/login', data={
        'email': 'test_1@email.com',
        'password': 'P@$$w0rd'
    })
