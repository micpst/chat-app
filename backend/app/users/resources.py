from flask_login import login_required, current_user
from flask_restful import Resource, fields, marshal

from app.users.models import User

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
}


class UserList(Resource):
    @login_required
    def get(self):
        """
        Endpoint to get all registered users.
        """
        users = User.query.all()
        return [marshal(user, user_fields) for user in users], 200


class UserData(Resource):
    @login_required
    def get(self, user_id):
        """
        Endpoint to get data of desired user.
        """
        user = User.query.get(user_id)
        return marshal(user, user_fields)


class UserMeData(Resource):
    @login_required
    def get(self):
        """
        Endpoint to get data of authenticated user.
        """
        return marshal(current_user, user_fields)
