from flask import jsonify


class NotUniqueException(Exception):
    pass

class ExistedException(Exception):
    pass

class DoesNotExistsException(Exception):
    pass

class HttpException(Exception):
    pass


except_dict = {
    'LoginFailed': {
        'code': 403,
        'message': "Login Failed"
    },
    'NeedAuth': {
        'code': 403,
        'message': "Need Auth"
    },
    'NotPermission': {
        'code': 403,
        'message': "Not Permission"
    },
    'GrandTypeError': {
        'code': 400,
        'message': "Grand Type Error"
    },
    'ParamsError': {
        'code': 400,
        'message': "Parameter Error"
    }
}


def __init__(self, **kwargs):
    self.message = self.message.format(**kwargs)


def __str__(self):
    return self.message


def __repr__(self):
    return self.message


exceptions_list = []
bases = (HttpException,)
attrs = {
    '__init__': __init__,
    '__str__': __str__,
    '__repr__': __repr__
}


for (eklass_name, attr) in except_dict.items():
    attrs.update(attr)
    eklass = type(str(eklass_name), bases, attrs)
    exceptions_list.append(eklass)
    globals().update({eklass_name: eklass})
