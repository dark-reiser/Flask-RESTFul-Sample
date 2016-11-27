
from flask import Flask
from flask.ext.redis import FlaskRedis
from flask.ext.bcrypt import Bcrypt
from config import config

redis_store = FlaskRedis()
bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    redis_store.init_app(app)
    bcrypt.init_app(app)

    return app