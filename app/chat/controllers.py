from typing import List
from flask import Blueprint, jsonify, redirect, render_template, url_for
from flask_login import login_required, current_user
from sqlalchemy import func
from sqlalchemy.engine.row import Row
from sqlalchemy.orm import aliased
from sqlalchemy.orm.util import AliasedClass
from werkzeug.wrappers.response import Response

from app import db
from app.utils import to_dict
from app.auth.models import User
from app.chat.models import Message

chat: Blueprint = Blueprint('chat', __name__)


@chat.route('/', methods=['GET'])
@login_required
def home() -> Response:
    """
    Redirect to user chats page.
    """
    return redirect(url_for('chat.chats'))


@chat.route('/chats', methods=['GET'])
@login_required
def chats() -> str:
    """
    User chats page.
    """
    return render_template('main.html', user=current_user)


@chat.route('/api/users', methods=['GET'])
@login_required
def get_users() -> Response:
    """
    Endpoint to get all registered users.
    """
    users: List[Row] = db.session.query(User.id.label('userId'), User.name.label('userName')).all()
    return jsonify(list(map(dict, users)))


@chat.route('/api/users/me/chats', methods=['GET'])
@login_required
def get_chats() -> Response:
    """
    Endpoint to get all user chats with the label of the last message sent.
    """
    Recipient: AliasedClass = aliased(User)
    Sender: AliasedClass = aliased(User)

    messages: List[Row] = db.session \
        .query(Recipient.id.label('recipientId'),
               Recipient.name.label('recipientName'),
               Sender.id.label('senderId'),
               Sender.name.label('senderName'),
               Message.body,
               Message.created_at.label('createdAt'),
               func.max(Message.created_at)) \
        .filter((Message.sender_id == current_user.id) | (Message.recipient_id == current_user.id)) \
        .join(Recipient, (Recipient.id == Message.sender_id) & (Message.sender_id != current_user.id) |
                         (Recipient.id == Message.recipient_id) & (Message.recipient_id != current_user.id)) \
        .join(Sender, (Sender.id == Message.sender_id)) \
        .group_by(Recipient.id) \
        .all()
    return jsonify(list(map(dict, messages)))


@chat.route('/api/users/me/chats/<int:user_id>/messages', methods=['GET'])
@login_required
def get_chat_messages(user_id: int) -> Response:
    """
    Endpoint to get all messages sent to and received from the user.
    """
    messages: List[Message] = db.session \
        .query(Message) \
        .filter((Message.sender_id == current_user.id) & (Message.recipient_id == user_id) |
                (Message.sender_id == user_id) & (Message.recipient_id == current_user.id)) \
        .all()
    return jsonify(list(map(to_dict, messages)))
