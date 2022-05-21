from flask_restful import Resource

from app import db
from app.users.models import User


class Login(Resource):
    def post(self):
        return {'test': 'login'}, 200


class Logout(Resource):
    def post(self):
        return {'test': 'logout'}, 200


class Signup(Resource):
    def post(self):
        return {'test': 'signup'}, 200
