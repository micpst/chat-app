from typing import List
from flask import Blueprint, jsonify, redirect, render_template, Response, url_for
from flask_login import login_required, current_user

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
    users: List[User] = User.query.all()
    return jsonify([{'id': user.id, 'name': user.name} for user in users])


@chat.route('/api/users/<int:user_id>/messages')
@login_required
def get_channel_messages(user_id: int) -> Response:
    """
    Endpoint to get all messages sent to and received from the user.
    """
    messages: List[Message] = Message.query.filter_by(sender_id=current_user.id, recipient_id=user_id).all()
    return jsonify([
        {
            'id': message.id,
            'content': message.content,
            'sender_id': message.sender_id,
            'recipient_id': message.recipient_id,
        }
        for message in messages
    ])
