import jwt
from common.config import Config
from datetime import datetime, timedelta
from common import constant
from common.constant import UTF_ENCODING


def generate_jwt_token(email, exp_time, **kwargs):
    """
    generate JWT token as temporary token
    """
    token = jwt.encode(
        {"email": email, "exp": datetime.utcnow() + timedelta(minutes=exp_time), **kwargs},
        Config.app_secret_key
    )
    return token


def decode_jwt_token(token):
    # a = token.decode(UTF_ENCODING)
    # c = Config.app_secret_key
    decoded = jwt.decode(token, Config.app_secret_key, algorithms=[constant.JWT_ENCRYPTION_ALGO], options={"verify_signature": False})
    return decoded
