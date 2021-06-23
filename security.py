import hashlib
from werkzeug.security import safe_str_cmp

from models.user import UserModel


def authenticate(username, password):
    user = UserModel.query.filter_by(username=username).first()
    if user:
        salt = user.password[:32]    
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        if key == user.password[32:]:
            return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.query.filter_by(id=user_id).first()