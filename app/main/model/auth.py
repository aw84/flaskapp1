import datetime
import jwt


def create_token(user_id, app_secret_key):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app_secret_key,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def get_token_subject(auth_token, app_secret_key):
    try:
        payload = jwt.decode(auth_token, app_secret_key, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
