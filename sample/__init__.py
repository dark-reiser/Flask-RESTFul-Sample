from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_bcrypt import Bcrypt
from flask_restless import APIManager
from flask_restful import Api
from config import config

db = SQLAlchemy()
rdb = FlaskRedis()
bcrypt = Bcrypt()
restless = APIManager()
api = Api()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    rdb.init_app(app)
    bcrypt.init_app(app)
    restless.init_app(app)
    api.init_app(app)

    from sample.api.views import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    from sample.auth.views import auth_bp as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @app.before_first_request
    def create_database():
        db.create_all()

    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
            "code": 400,
            "message": "Bad Request"
        })


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "code": 404,
            "message": "Not Found"
        })


    @app.errorhandler(405)
    def method_not_support(error):
        return jsonify({
            "code": 405,
            "message": "Method Not Support"
        })


    @app.errorhandler(exception.HttpException)
    def http_exception(error):
        return jsonify({
            "code": error.code,
            "message": error.message
        })


    @app.errorhandler(Exception)
    def internel_error(error):
        return jsonify({
            "code": 500,
            "message": "Internal Error"
        })

    return app