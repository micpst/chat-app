from flask import Blueprint
from flask_restful import Api

from app.users.resources import UserData, UserMeData, UserList

users_bp: Blueprint = Blueprint('users', __name__)
users_api: Api = Api(users_bp)

users_api.add_resource(UserList, '/users')
users_api.add_resource(UserMeData, '/users/me')
users_api.add_resource(UserData, '/users/<int:user_id>')
