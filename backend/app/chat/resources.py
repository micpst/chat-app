from flask import jsonify
from flask_login import current_user
from flask_restful import Resource
from sqlalchemy.orm import aliased

from app import db
from app.users.models import User
from app.chat.models import Message
from app.utils import to_dict


class ChatList(Resource):
    def get(self):
        """
        Endpoint to get all user chats with the label of the last message sent.
        """
        Recipient = aliased(User)
        Sender = aliased(User)

        messages = db.session \
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

        return list(map(dict, messages)), 200


class ChatData(Resource):
    def get(self, user_id):
        """
        Endpoint to get all messages sent to and received from the user.
        """
        messages = db.session \
            .query(Message) \
            .filter((Message.sender_id == current_user.id) & (Message.recipient_id == user_id) |
                    (Message.sender_id == user_id) & (Message.recipient_id == current_user.id)) \
            .all()

        return list(map(to_dict, messages)), 200
