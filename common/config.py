import os
from os import environ
from cryptography.fernet import Fernet

secret_key = os.urandom(32)
# FERNET = "k-1k6diILafCUt63-IooJplOybLy1i_hsft4gzXvt_Q\="

# FERNET = Fernet.generate_key()

# app.config['SECRET_KEY'] = secret_key
class Config:
    app_secret_key = environ.get("SECRET_KEY", secret_key)
    FERNET_KEY = environ.get("FERNET_KEY")
