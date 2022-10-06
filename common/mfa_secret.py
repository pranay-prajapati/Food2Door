import pyotp
from os import environ

from common.config import Config
from common.constant import UTF_ENCODING, MFA_EXP_TIME_IN_SECONDS
from cryptography.fernet import Fernet


def encrypt_mfa_secret(obj_str):
    """
    Encryption of MFA secret key
    """
    key = bytes(Config.FERNET_KEY, UTF_ENCODING)
    fernet = Fernet(key)
    encoded = fernet.encrypt(obj_str.encode())
    return encoded


def decrypt_mfa_secret(obj):
    """
    Encryption of MFA secret key
    """
    key = Config.FERNET_KEY
    fernet = Fernet(key)
    return fernet.decrypt(bytes(obj, UTF_ENCODING)).decode()


def send_mfa(mfa_secret):
    mfa_code = pyotp.TOTP(mfa_secret, interval=MFA_EXP_TIME_IN_SECONDS).now()
    return mfa_code
