from flask import Blueprint, render_template, redirect, url_for, Response
from flask_login import login_required, current_user

main: Blueprint = Blueprint('main', __name__)


@main.route('/')
@login_required
def home() -> Response:
    """
    Redirect to user chats page.
    """
    return redirect(url_for('main.chats'))


@main.route('/chats')
@login_required
def chats() -> str:
    """
    User chats page.
    """
    return render_template("main.html", user=current_user)
