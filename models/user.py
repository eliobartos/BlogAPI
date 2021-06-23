from db import db
import hashlib
import os

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.LargeBinary(1024))

    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def __str__(self):
        return f'User: {self.username}, id: {self.id}'

    def save_to_db(self):
        db.session.add(self)
        print("HEREEE")
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @staticmethod
    def hash_password(password):
        salt = os.urandom(32)
        print(f"Salt: {salt}")
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        print(f"Key: {key}")
        return salt + key