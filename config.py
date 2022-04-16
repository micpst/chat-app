from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath(path.dirname(__file__)), '.env'))


SECRET_KEY = environ.get('SECRET_KEY')
SERVER = environ.get('SERVER')
SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
TESTING = environ.get('TESTING')
