from flask_login import current_user, login_required
from flask_restful import Resource, fields, marshal
from sqlalchemy.orm import aliased

from app import db
from app.chat.models import Message
from app.users.models import User

chat_fields = {
    'recipientId': fields.Integer,
    'recipientName': fields.String,
    'senderId': fields.Integer,
    'senderName': fields.String,
    'body': fields.String,
    'createdAt': fields.DateTime
}

message_fields = {
    'recipientId': fields.Integer,
    'senderId': fields.Integer,
    'body': fields.String,
    'createdAt': fields.DateTime
}


class ChatList(Resource):
    @login_required
    def get(self):
        """
        Endpoint to get all user chats with the label of the last message sent.
        """
        Recipient = aliased(User)
        Sender = aliased(User)

        chats = db.session \
            .query(Recipient.id.label('recipientId'),
                   Recipient.name.label('recipientName'),
                   Sender.id.label('senderId'),
                   Sender.name.label('senderName'),
                   Message.body,
                   Message.created_at.label('createdAt')) \
            .filter((Message.sender_id == current_user.id) | (Message.recipient_id == current_user.id)) \
            .join(Recipient, (Recipient.id == Message.sender_id) & (Message.sender_id != current_user.id) |
                             (Recipient.id == Message.recipient_id) & (Message.recipient_id != current_user.id)) \
            .join(Sender, (Sender.id == Message.sender_id)) \
            .distinct(Recipient.id) \
            .order_by(Recipient.id, Message.created_at.desc()) \
            .all()

        return [marshal(chat, chat_fields) for chat in chats], 200


class ChatData(Resource):
    @login_required
    def get(self, user_id):
        """
        Endpoint to get all messages sent to and received from the user.
        """
        messages = db.session \
            .query(Message.recipient_id.label('recipientId'),
                   Message.sender_id.label('senderId'),
                   Message.body,
                   Message.created_at.label('createdAt')) \
            .filter((Message.sender_id == current_user.id) & (Message.recipient_id == user_id) |
                    (Message.sender_id == user_id) & (Message.recipient_id == current_user.id)) \
            .all()

        return [marshal(message, message_fields) for message in messages], 200
