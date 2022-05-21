from flask import Blueprint
from flask_restful import Api

import app.chat.events
from app.chat.resources import ChatData, ChatList

chat_bp: Blueprint = Blueprint('chat', __name__)
chat_api: Api = Api(chat_bp)

chat_api.add_resource(ChatList, '/chats')
chat_api.add_resource(ChatData, '/chats/<int:user_id>')
