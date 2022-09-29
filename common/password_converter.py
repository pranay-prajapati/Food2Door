import hashlib
from common import constant


def generate_password_hash(obj):
    """
    Hashes given object with hashlib.sha224 algorithm. Return string.
    """
    return hashlib.sha256(str(obj).encode(constant.UTF_ENCODING)).hexdigest()
