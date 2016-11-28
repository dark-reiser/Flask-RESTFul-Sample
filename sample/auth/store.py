from werkzeug import cached_property
from sample import exception
from sample import rdb
from sample import bcrypt

class OAuth2Store(object):
    """
    Interface for redis db.
    """

    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        self._redis_host = redis_host
        self._redis_port = redis_port
        self._redis_db = redis_db
        self._uid = self.get_init_uid()

    @cached_property
    def get_init_uid(self):
        uid = rdb.get('uid')
        if not uid:
            rdb.set('uid', 0)
            uid = rdb.get('uid')
        return uid

    def add_user(self, username, passwd):
        if rdb.hgetall('user:{}'.format(username)):
            raise exception.ExistedException
        else:
            passwd_hash = bcrypt.generate_password_hash(passwd)
            rdb.incr('uid')
            context = {'uid':rdb.get('uid'), 'username':username, 'passwd':passwd_hash}
            rdb.hmset('user:{}'.format(username), context)