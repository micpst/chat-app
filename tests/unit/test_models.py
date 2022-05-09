from app.auth.models import User
from app.chat.models import Message


def test_new_user():
    """
    Given a User model
    When a new User is created
    Then check the id, name, email and password fields are defined correctly
    """
    user = User('Michal', 'michal.contact@gmail.com', 'MyP@$$w0rd')

    assert user.id is None
    assert user.name == 'Michal'
    assert user.email == 'michal.contact@gmail.com'
    assert user.verify_password('MyP@$$w0rd')


def test_new_message():
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
