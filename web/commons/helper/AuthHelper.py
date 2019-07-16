from datetime import datetime, timedelta
import jwt
from web import app, bcrypt


def generate_jwt_token(user_id):
    payload = {
        'exp': datetime.now() + timedelta(minutes=app.config.get('AUTH_TOKEN_MINUTES')),
        'iat': datetime.now(),
        'sub': user_id
    }
    print(payload)
    return jwt.encode(
        payload=payload,
        key=app.config.get('SECRET_KEY'),
        algorithm='HS512'
    )


def generate_hash_for_password(password):
    return bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS'))


def validate_password(hash, password):
    return bcrypt.check_password_hash(hash, password)


def decode_jwt_token(token):
    decoded_data = jwt.decode(token, app.config.get('SECRET_KEY'))
    user_id = decoded_data['sub']
    from web.auth.models.AuthModel import AuthModel
    auth_model = AuthModel()
    user_data = auth_model.check_user_by_id(user_id)
    if not user_data.isAdmin:
        return False
    return True
