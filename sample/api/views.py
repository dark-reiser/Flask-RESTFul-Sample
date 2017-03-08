from flask import request, jsonify
from .. import db
from .. import restless
from .. import rdb
from . import api_bp
from sample.models import User, Client
from sample.validator import validate
from sample.utils import need_auth, auth_source, verify_access_token
from sample import exception


@api_bp.route('/test', methods=['GET'])
@need_auth
@auth_source
def test():
    return jsonify({
        "code": 200,
        "data": "OK"
        })