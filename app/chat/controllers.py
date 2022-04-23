from typing import List
from flask import Blueprint, jsonify, redirect, render_template, url_for
from flask_login import login_required, current_user
from sqlalchemy import func
from sqlalchemy.engine.row import Row
from werkzeug.wrappers.response import Response

from app import db
from app.utils import to_dict
from app.auth.models import User
from app.chat.models import Message

chat: Blueprint = Blueprint('chat', __name__)


@chat.route('/')
@login_required
def home() -> Response:
    """
    Redirect to user chats page.
    """
    return redirect(url_for('chat.chats'))


@chat.route('/chats')
@login_required
def chats() -> str:
    """
    User chats page.
    """
    return render_template("main.html", user=current_user)


@chat.route('/api/users')
@login_required
def get_users() -> Response:
    """
    Endpoint to get all registered users.
    """
    users: List[Row] = db.session.query(User.id, User.name).all()
    return jsonify(list(map(dict, users)))


@chat.route('/api/users/me/chats')
@login_required
def get_chats() -> Response:
    """
    Endpoint to get all user chats with the label of the last message sent.
    """
    messages: List[Row] = db.session\
        .query(User.id, User.name, Message.sender_id, Message.body, Message.created_at, func.max(Message.created_at))\
        .filter((Message.sender_id == current_user.id) | (Message.recipient_id == current_user.id))\
        .join(User,
              (User.id == Message.sender_id) & (Message.sender_id != current_user.id) |
              (User.id == Message.recipient_id) & (Message.recipient_id != current_user.id)
              )\
        .group_by(User.id)\
        .all()
    return jsonify(list(map(dict, messages)))


@chat.route('/api/users/me/chats/<int:user_id>/messages')
@login_required
def get_chat_messages(user_id: int) -> Response:
    """
    Endpoint to get all messages sent to and received from the user.
    """
    messages: List[Message] = db.session.query(Message).filter(
        (Message.sender_id == current_user.id) & (Message.recipient_id == user_id) |
        (Message.sender_id == user_id) & (Message.recipient_id == current_user.id)
    ).all()
    return jsonify(list(map(to_dict, messages)))
