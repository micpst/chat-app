import pytest

from app import create_app, db


@pytest.fixture
def app():
    return create_app('testing')


@pytest.fixture(scope='function')
def database(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
    yield db