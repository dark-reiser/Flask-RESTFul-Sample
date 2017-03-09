from . import bcrypt
from . import db


class BaseMixin:
    def to_dict(self, exclude_columns=None):
        if exclude_columns is None:
            exclude_columns = []
        d = {}
        for column in self.__table__.columns:
            if unicode(column.name) in exclude_columns:
                continue
            d[column.name] = getattr(self, column.name)

        return d


class User(db.Model):
    """
    User.
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    passwd_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

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
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String(128), nullable=False)


class Student(db.Model, BaseMixin):
    """
    Student
    """

    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    profession = db.Column(db.String(128), nullable=False)
