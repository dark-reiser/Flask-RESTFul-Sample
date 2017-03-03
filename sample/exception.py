class NotUniqueException(Exception):
    pass

class ExistedException(Exception):
    pass

class DoesNotExistsException(Exception):
    pass

class NeedAuth(Exception):
    pass

class ParamsError(Exception):
    pass

class GrandTypeError(Exception):
    pass

class LoginFailed(Exception):
    pass

class NotPermission(Exception):
    pass

class HttpException(Exception):
    pass