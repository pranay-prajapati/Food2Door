import os
from os import environ

secret_key = os.urandom(32)
FERNET = "k-1k6diILafCUt63-IooJplOybLy1i_hsft4gzXvt_Q\="


# app.config['SECRET_KEY'] = secret_key
class Config:
    app_secret_key = environ.get("SECRET_KEY", secret_key)
    FERNET_KEY = environ.get("FERNET_KEY", FERNET)
