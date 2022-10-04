import os
from os import environ

secret_key = os.urandom(32)


# app.config['SECRET_KEY'] = secret_key
class Config:
    app_secret_key = environ.get("SECRET_KEY", secret_key)
