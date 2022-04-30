if __name__ == '__main__':
    from os import getenv
    from app import create_app, socketio

    app = create_app(getenv('FLASK_CONFIG'))
    socketio.run(app, host='0.0.0.0')
