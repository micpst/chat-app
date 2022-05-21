from os import getenv


class Config:
    """
    Base configuration
    """

    user = getenv('POSTGRES_USER')
    password = getenv('POSTGRES_PASSWORD')
    hostname = getenv('POSTGRES_HOSTNAME')
    port = getenv('POSTGRES_PORT')
    database = getenv('APPLICATION_DB')

    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{user}:{password}@{hostname}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    """
    Production configuration
    """


class DevelopmentConfig(Config):
    """
    Development configuration
    """


class TestingConfig(Config):
    """
    Testing configuration
    """

    database = getenv('APPLICATION_TEST_DB')

    TESTING = True
