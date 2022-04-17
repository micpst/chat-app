from typing import Optional, Union
from flask import Blueprint, flash, redirect, render_template, Response, request, url_for
from flask_login import login_required, login_user, logout_user

from app import db, login_manager
from app.auth.forms import LoginForm, SignupForm
from app.auth.models import User

auth: Blueprint = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id: Optional[str]) -> Optional[User]:
    """
    Check if user is logged-in on every page load.
    """
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized() -> Response:
    """
    Redirect unauthorized users to login page.
    """
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup() -> Union[str, Response]:
    """
    Signup page for unregistered users.
    """
    form: SignupForm = SignupForm(request.form)

    if form.validate_on_submit():
        user: Optional[User] = User.query.filter_by(email=form.email.data).first()

        if user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data
            )

            db.session.add(user)
            db.session.commit()

            login_user(user)
            return redirect(url_for('main.chats'))

        flash('User already exists.')

    return render_template("signup.html", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login() -> Union[str, Response]:
    """
    Login page for registered users.
    """
    form: LoginForm = LoginForm(request.form)

    if form.validate_on_submit():
        user: Optional[User] = User.query.filter_by(email=form.email.data).first()

        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.chats'))

        flash('Invalid email or password.')

    return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout() -> Response:
    """
    Logout current user and redirect to the login page.
    """
    logout_user()
    flash("You were logged out.")
    return redirect(url_for("auth.login"))
