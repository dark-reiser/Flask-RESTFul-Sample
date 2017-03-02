from flask import request, jsonify
from app.app import restless
from app.app import db
from app.app import rdb
from . import auth
from store import TokenStore, generate_token
from user import User, Client
from sample.validator import validate
from utils import verify, verify_refresh_token, verify_access_token
from utils import need_auth, auth_source
from sample import exception

auth.route('/oauth', method=['POST'])
def access():
    validate('type_validate', request.json)

    if request.json['grand_type'] == 'password':
        validate('password_login', request.json)
        user = verify(request.json)
        if not user:
            raise exceptions.LoginFailed

        access_token = TokenStore(user.id, request.json['client_id'], generate_token())
        refresh_token = TokenStore(user.id, request.json['client_id'], generate_token(), token_type='Refresh',)        

        return jsonify({
            "access_token": access_token.token,
            "refresh_token": refresh_token.token
            })

    elif request.json['grand_type'] == 'refresh_token':
        validate('refresh_login', request.json)
        refresh_token = verify_refresh_token(request.json['refresh_token'])
        if not refresh_token:
            raise exceptions.LoginFailed

        access_token = TokenStore(refresh_token['uid'], refresh_token['client_id'], generate_token())

        return jsonify({
            "access_token": access_token.token
            })

    else:
        raise exceptions.GrandTypeError

    return jsonify({
        "code": 0,
        "data": user
    })




@need_auth
@auth_source
def _user_get_many(*args, **kwargs):
    search_params = kwargs['search_params']

    if search_params is None:
        return

    if 'filters' not in search_params:

        user = session['user']
        search_params['filters'] = []
        filt = None

        if filt:
            search_params['filters'].append(filt)


_url_prefix = '/auth'
restless.create_api(User
                    , collection_name="user"
                    , methods=['GET', 'POST', 'PUT', 'DELETE']
                    , exclude_columns=['password']
                    , url_prefix=_url_prefix
                    , preprocessors={"GET_MANY":[_user_get_many]}
                )