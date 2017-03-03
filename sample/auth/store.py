import uuid
from werkzeug import cached_property
from sample import exception
from .. import rdb
from itsdangerous import JSONWebSignatureSerializer


class TokenStore(object):
    """
    Interface for token.
    """

    def __init__(self, uid, client_id, token, token_type='Access', expires=3600):
        self.token = token
        self.token_type = token_type
        self.uid = uid
        self.client_id = client_id
        if token_type == 'Refresh':
            self.expires = expires*24
        else:
            self.expires = expires

    def save(self):
        context = {'token_type':self.token_type, 'uid':self.uid, 'client_id':self.client_id}
        rdb.hmset('{}'.format(self.token), context)
        rdb.expire(self.token, self.expires)
        return None


def generate_token():
    token = JSONWebSignatureSerializer('SECRET-KEY').dumps(uuid.uuid1().hex)
    return token