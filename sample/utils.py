import functools
from flask import request
from . import rdb
from . import db
from sample.models import User, Client
from sample import exception


def need_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        if "authorization" not in request.headers:
            raise exception.NeedAuth

        return func(*args, **kwargs)
    return wrapper


def auth_source(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        access_token = request.headers['authorization']
        if rdb.hgetall(access_token):
            pass
        else:
            raise exception.NotPermission

        return func(*args, **kwargs)
    return wrapper


def verify_access_token(token):
    if rdb.hget(token, 'token_type') == 'Access':
        return rdb.hmget(token, 'uid', 'client_id')

    else:
        return False