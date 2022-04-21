from flask import Flask
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
login_manager: LoginManager = LoginManager()
socketio: SocketIO = SocketIO()


def create_app() -> Flask:
    """
    Application factory.
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        from app.auth.controllers import auth
        from app.chat.controllers import chat

        app.register_blueprint(auth)
        app.register_blueprint(chat)

        db.create_all()

    return app
