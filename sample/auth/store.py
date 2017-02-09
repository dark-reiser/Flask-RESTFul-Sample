import uuid
from werkzeug import cached_property
from sample import exception
from sample import rdb
from sample import bcrypt
from itsdangerous import JSONWebSignatureSerializer

class OAuth2Store(object):
    """
    Interface for basic OAuth information.
    """

    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0, password=None):
        self._redis_host = redis_host
        self._redis_port = redis_port
        self._redis_db = redis_db
        self._uid = self.get_init_uid()



    def add_user(self, username, passwd, expires=None):
        if rdb.hgetall('user:{}'.format(username)):
            raise exception.NotUniqueException
        else:
            passwd_hash = bcrypt.generate_password_hash(passwd)
            rdb.incr('uid')
            context = {'uid':rdb.get('uid'), 'username':username, 'passwd':passwd_hash}
            rdb.hmset('user:{}'.format(username), context)
            return True

    def add_client(self, client_id, client_secret):
        if rdb.hgetall('client:{}'.format(client_id)):
            raise exception.ExistedException
        else:
            secret_hash = bcrypt.generate_password_hash(client_secret)
            context = {'client_id':client_id, 'client_secret':secret_hash}
            rdb.hmset('client:{}'.format(client_id), context)
            return True

class TokenStore(object):
    """
    Interface for token.
    """

    def __init__(self, token, token_type='Access', uid, client_id, expires=3600):
        self._token = token
        self._token_type = token_type
        self._uid = uid
        self._client_id = client_id
        if token_type == 'Refresh':
            self.expires = expires*24
        else:
            self.expires = expires

    def save(self):
        context = {'token_type':self._token_type, 'uid':self._uid, 'client_id':self._client_id}
        rdb.hmset('{}'.format(self._token), context)
        rdb.expire(self._token, self.expires)
        return None

def generate_token():
    token = JSONWebSignatureSerializer('SECRET-KEY').dumps(uuid.uuid1().hex)
    return token