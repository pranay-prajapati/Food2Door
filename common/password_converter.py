import hashlib
from common import constant
from exception.http_exception import HttpException


def generate_password_hash(obj):
    """
    Hashes given object with hashlib.sha224 algorithm. Return string.
    """
    return hashlib.sha256(str(obj).encode(constant.UTF_ENCODING)).hexdigest()


def compare_password_hash(old, new):
    """
    Compare old and new password hash
    """
    if new == old:
        raise HttpException("Password cannot be same.", constant.ENTITY_EXISTS, 400)
