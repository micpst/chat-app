from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath(path.dirname(__file__)), '.env'))


class Config:
    ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')
    SERVER = environ.get('SERVER')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = environ.get('TESTING')
