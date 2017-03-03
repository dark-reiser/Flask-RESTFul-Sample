from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_bcrypt import Bcrypt
from flask_restless import APIManager
from config import config

db = SQLAlchemy()
rdb = FlaskRedis()
bcrypt = Bcrypt()
restless = APIManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    rdb.init_app(app)
    bcrypt.init_app(app)
    restless.init_app(app)

    from sample.auth import auth_bp as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from sample.api import api_bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    @app.before_first_request
    def create_database():
        db.create_all()

    # @app.errorhandler(400)
    # def not_found(error):
    #     return jsonify({
    #         "code": 400,
    #         "message": "BadRequest"
    #     })


    # @app.errorhandler(404)
    # def not_found(error):
    #     return jsonify({
    #         "code": 404,
    #         "message": "NotFound"
    #     })


    # @app.errorhandler(405)
    # def method_not_support(error):
    #     return jsonify({
    #         "code": 405,
    #         "message": "MethodNotSupport"
    #     })


    # @app.errorhandler(exception.HttpException)
    # def http_exception(error):
    #     return jsonify({
    #         "code": error.code,
    #         "message": error.message
    #     })


    # @app.errorhandler(Exception)
    # def internel_error(error):
    #     return jsonify({
    #         "code": 500,
    #         "message": "Internal Error"
    #     })

    return app