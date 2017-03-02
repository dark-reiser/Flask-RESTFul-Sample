from cerberus import Validator

from . import exception


_v = {
    'type_validate': {
        'grand_type': {
            'required': True
        },
    },
    'password_login': {
        'username': {
            'required': True
        },
        'password': {
            'required': True
        },
        'client_id': {
            'required': True
        },
        'client_secret': {
            'required': True
        },
    },
    'refresh_login': {
        'refresh_token': {
            'required': True
        },
    },
}

def validate(key, params):
    v = Validator()
    v.allow_unknown = True
    v.validate(params, _v[key])

    if v.errors:
        raise exceptions.ParamsError

    return True