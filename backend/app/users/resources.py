from flask_restful import Resource

from app import db
from app.users.models import User


class UserList(Resource):
    def get(self):
        """
        Endpoint to get all registered users.
        """
        users = db.session.query(User.id, User.name).all()
        return list(map(dict, users))


class UserData(Resource):
    def get(self, user_id):
        return {'message': f'user #{user_id} get'}, 200

    def put(self, user_id):
        return {'message': f'user #{user_id} put'}, 200

    def delete(self, user_id):
        return {'message': f'user #{user_id} delete'}, 200
