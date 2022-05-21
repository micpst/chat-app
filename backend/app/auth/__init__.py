from flask import Blueprint
from flask_restful import Api

from app.auth.resources import Login, Logout, Signup

auth_bp: Blueprint = Blueprint('auth', __name__)
auth_api: Api = Api(auth_bp)

auth_api.add_resource(Login, '/auth/login')
auth_api.add_resource(Logout, '/auth/logout')
auth_api.add_resource(Signup, '/auth/signup')
