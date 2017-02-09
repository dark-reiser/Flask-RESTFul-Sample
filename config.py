import os

class BaseConfig(object):
    SECRET_KEY = 'SECRET_KEY'

    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

    REDIS_URL = 'redis://localhost:6379/0'

    SQLALCHEMY_DATABASE_URL = None

    DEBUG = False

class DevelopmentConfig(BaseConfig):
    SECRET_KEY = 'RND_SECRET_KEY_VALUE'

    DEBUG = True

    SQLALCHEMY_DATABASE_URL = None


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}