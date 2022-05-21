from sqlalchemy import func

from app import db
from app.users.models import User


class Message(db.Model):

    __tablename__: str = 'message'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    body = db.Column(
        db.String(100),
        nullable=False,
        unique=False
    )

    sender_id = db.Column(
        db.Integer,
        db.ForeignKey(User.id),
        nullable=False,
        unique=False
    )

    recipient_id = db.Column(
        db.Integer,
        db.ForeignKey(User.id),
        nullable=False,
        unique=False
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        unique=False
    )

    def __init__(self, body: str, sender_id: int, recipient_id: int) -> None:
        self.body = body
        self.sender_id = sender_id
        self.recipient_id = recipient_id

    def __repr__(self) -> str:
        return f"<Message body='{self.body}' from={self.sender_id} to={self.recipient_id}>"
