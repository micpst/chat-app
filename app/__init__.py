from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
login_manager: LoginManager = LoginManager()
migrate: Migrate = Migrate()
socketio: SocketIO = SocketIO()


def create_app(config_name: str) -> Flask:
    """
    Application factory.
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    with app.app_context():
        from app.auth.controllers import auth
        from app.chat.controllers import chat

        app.register_blueprint(auth)
        app.register_blueprint(chat)

    return app
