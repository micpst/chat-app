import pytest

from app import create_app, db, socketio


@pytest.fixture(scope='module')
def app():
    return create_app('testing')


@pytest.fixture(scope='module')
def app_client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture(scope='module')
def sio_client(app, app_client):
    return socketio.test_client(app, flask_test_client=app_client)


@pytest.fixture(scope='function')
def database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
    return db
