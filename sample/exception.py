from flask import jsonify


class NotUniqueException(Exception):
    pass

class ExistedException(Exception):
    pass

class DoesNotExistsException(Exception):
    pass

class NeedAuth(Exception):
    return jsonify(
        "code": 403,
        "message": "Not Authenticated"
        )

class ParamsError(Exception):
    return jsonify(
        "code": 400,
        "message": "Params Error"
        )

class GrandTypeError(Exception):
    return jsonify(
        "code": 400,
        "message": "Grand Type Error"
        )

class LoginFailed(Exception):
    return jsonify(
        "code": 403,
        "message": "Login Failed"
        )

class NotPermission(Exception):
    return jsonify(
        "code": 403,
        "message": "Not Permission"
        )

class HttpException(Exception):
    pass