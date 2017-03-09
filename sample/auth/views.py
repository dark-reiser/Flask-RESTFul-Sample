from flask import request, jsonify, Blueprint
from .. import db
from .. import restless
from .. import rdb
from store import TokenStore, generate_token
from sample.models import User, Client
from sample.validator import validate
from utils import verify, verify_refresh_token
from sample.utils import need_auth, auth_source, verify_access_token
from sample import exception


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/oauth', methods=['POST'])
def access():
    validate('type_validate', request.json)

    if request.json['grand_type'] == 'password':
        validate('password_login', request.json)

        user = verify(request.json)
        if not user:
            raise exception.LoginFailed()

        access_token = TokenStore(user.id, request.json['client_id'], generate_token())
        refresh_token = TokenStore(user.id, request.json['client_id'], generate_token(), token_type='Refresh')

        access_token.save()
        refresh_token.save()

        return jsonify({
            "access_token": access_token.token,
            "refresh_token": refresh_token.token
            })

    elif request.json['grand_type'] == 'refresh_token':
        validate('refresh_login', request.json)
        refresh_token = verify_refresh_token(request.json['refresh_token'])
        if not refresh_token:
            raise exception.LoginFailed()

        access_token = TokenStore(refresh_token[0], refresh_token[1], generate_token())

        access_token.save()

        return jsonify({
            "access_token": access_token.token
            })

