import os
from flask import Flask
from service.user.routes import user_management_route
from service.food.routes import food_management_route
from common.config import Config

def create_app():
    app = Flask(__name__)
    app.config["WTF_CSRF_ENABLED"] = False

    # secret_key = os.urandom(32)
    app.config['SECRET_KEY'] = Config.app_secret_key

    # register blueprint
    app.register_blueprint(user_management_route,
                           url_prefix="/api/v1/users")
    app.register_blueprint(food_management_route,
                           url_prefix="/api/v1/foods")

    return app
