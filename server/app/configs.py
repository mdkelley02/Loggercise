import os

class DevelopmentConfig(object):
    DEBUG = True
    SECRET_KEY = os.urandom(20)
    SQLALCHEMY_DATABASE_URI = "sqlite:///development.db"
    FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_CONNECTION_STRING")
    FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False