
"""
Create an application instance.
"""

import os

class BaseConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

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