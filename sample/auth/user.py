from sample import bcrypt
from sample import db

class User(db.Model):
    """
    User.
    """

    __tablename__ = 'users'
    id = db.Column(db.Interger)
    username = db.Column(db.String(64), nullable=False, primary_key=True)
    passwd_hash = db.Column(db.String(128))

    @property
    def passwd(self):
        raise AttributeError('passwd is not a readable attribute.')

    @passwd.setter
    def passwd(self, passwd):
        self.passwd_hash = bcrypt.generate_passwd_hash(passwd)

    def verify_passwd(self, passwd):
        return bcrypt.check_password_hash(self.passwd_hash, passwd)

class Client(db.Model):
    """
    Client.
    """

    __talblename__ = 'clients'
    id = db.Column(db.Interger, primary_key=True)
    secret = db.Column(db.String(128))