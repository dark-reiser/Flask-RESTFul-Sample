from flask import Flask
from flask.ext.redis import FlaskRedis
from flask.ext.bcrypt import Bcrypt
from config import config

rdb = FlaskRedis()
bcrypt = Bcrypt()

def create_app(config_name):
    """
    Entry point to the Flask RESTFul Server application.
    """

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    rdb.init_app(app)
    bcrypt.init_app(app)

    from sample.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from sample.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app