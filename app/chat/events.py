from typing import Any, Dict, Optional
from flask_login import current_user
from flask_socketio import close_room, emit, join_room

from app import db, socketio
from app.chat.models import Message
from app.auth.models import User


@socketio.on('connect')
def handle_connect() -> bool:
    """
    Handler to authorize client and join user to his room.
    """
    if not current_user.is_authenticated:
        return False

    join_room(current_user.id)
    return True


@socketio.on('disconnect')
def handle_disconnect() -> None:
    """
    Handler to close client room.
    """
    close_room(current_user.id)


@socketio.on('send')
def handle_send(json: Optional[Dict[str, Any]] = None) -> None:
    """
    Handler to save client message and send it to the recipient.
    """
    json = json or {}

    body: str = json.get('body', '')
    recipient_id: int = json.get('recipientId', -1)

    user: Optional[User] = User.query.filter_by(id=recipient_id).first()
    if user is None:
        raise RuntimeError('User not found.')

    message: Message = Message(
        body=body,
        sender_id=current_user.id,
        recipient_id=recipient_id
    )
    db.session.add(message)
    db.session.commit()

    emit('receive', {'body': 'test'}, to=recipient_id)


@socketio.on_error()
def handle_error(message: str):
    """
    Handler to emi.
    """
    emit('error', {'message': message})
