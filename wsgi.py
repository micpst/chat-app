from os import getenv
from app import create_app, socketio

app = create_app(getenv('FLASK_CONFIG'))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
