from flask_login import login_user, login_required, logout_user
from flask_restful import Resource, reqparse

from app import db, login_manager
from app.auth.validators import email, length
from app.users.models import User


@login_manager.user_loader
def load_user(user_id):
    """
    Check if user is logged-in on every request.
    """
    if user_id is not None:
        return User.query.get(user_id)

    return None


@login_manager.unauthorized_handler
def unauthorized():
    """
    Send unauthorized response object.
    """
    return {'message': 'Unauthorized access'}, 401


class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=email, required=True, trim=True, nullable=False)
        self.parser.add_argument('password', type=length(8, 80), required=True, trim=True, nullable=False)

    def post(self):
        args = self.parser.parse_args()
        user = User.query.filter_by(email=args.email).first()

        if user and user.verify_password(args.password):
            login_user(user)
            return {'message': 'Successfully logged in'}, 200

        return {'message': 'Invalid email or password'}, 404


class Logout(Resource):
    @login_required
    def post(self):
        logout_user()
        return {'message': 'Successfully logged out'}, 200


class Signup(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=length(1, 15), required=True, trim=True, nullable=False)
        self.parser.add_argument('email', type=email, required=True, trim=True, nullable=False)
        self.parser.add_argument('password', type=length(8, 80), required=True, trim=True, nullable=False)

    def post(self):
        args = self.parser.parse_args()
        user = User.query.filter_by(email=args.email).first()

        if user is None:
            user = User(**args)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return {'message': 'Successfully registered'}, 201

        return {'message': 'User already exists'}, 400
