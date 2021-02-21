import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'test-secret-key')
    DEBUG = False


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/flaskapp1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=Development
)
