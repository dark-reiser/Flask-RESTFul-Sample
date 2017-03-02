import functools
from flask import request
from sample import rdb
from sample import db
from user import User, Client
from sample import exception

def need_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        if 'authorization' not in request.header:
            raise exception.NeedAuth

        return func(*args, **kwargs)
    return wrapper


def auth_source(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        access_token = request.header['authorization']
        if rdb.hmgetall(access_token):
            pass
        else:
            raise exception.NotPermission

        return func(*args, **kwargs)
    return wrapper


def verify(data):
    user = User.query.filter_by(username=data['username']).first()
    if user is None:
        return False

    if not user.verify_passwd(data['password']):
        return False

    client = Client.query.filter_by(id=data['client_id']).first()
    if client is None:
        return False

    if client.secret != data['client_secret']:
        return False

    return user.id


def verify_refresh_token(token):
    if rdb.hmget(token, 'token_type') == 'Refresh':
        return rdb.hmget(token, 'uid', 'client_id')

    else:
        return False


def verify_access_token(token):
    if rdb.hmget(token, 'token_type') == 'Access':
        return rdb.hmget(token, 'uid', 'client_id')

    else:
        return False