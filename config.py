import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'RND_SECRET_KEY_VALUE'
    SSL_DISABLE = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
       'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    REDIS_URL = 'redis://localhost:6379/0'
    # SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:fortinet@127.0.0.1/test'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}