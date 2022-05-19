import pytest

from app.auth.models import User
from app.chat.models import Message


def test_new_user(db):
    """
    Given a User model
    When a new User is created
    Then check the id, name, email and password fields are defined correctly
    """
    user = User('test', 'test@email.com', 'P@$$w0rd')

    assert user.id is None
    assert user.name == 'test'
    assert user.email == 'test@email.com'
    assert user.verify_password('P@$$w0rd')

    db.session.add(user)
    db.session.commit()

    assert user.id == 1
    assert user.name == 'test'
    assert user.email == 'test@email.com'
    assert user.verify_password('P@$$w0rd')


@pytest.mark.usefixtures('db_users')
def test_new_message(db):
    """
    Given a Message model
    When a new Message is created
    Then check the id, body, sender_id, recipient_id, created_at fields are defined correctly
    """
    message = Message('Hi', 1, 2)

    assert message.id is None
    assert message.body == 'Hi'
    assert message.sender_id == 1
    assert message.recipient_id == 2
    assert message.created_at is None

    db.session.add(message)
    db.session.commit()

    assert message.id == 1
    assert message.body == 'Hi'
    assert message.sender_id == 1
    assert message.recipient_id == 2
    assert message.created_at is not None
