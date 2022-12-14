import os
from flask import Flask
from service.user.routes import user_management_route
from service.food.routes import food_management_route
from service.restaurant.routes import restaurant_management_route
from common.config import Config


def create_app():
    app = Flask(__name__)
    app.config["WTF_CSRF_ENABLED"] = False

    app.config['SECRET_KEY'] = Config.app_secret_key

    # register blueprint
    app.register_blueprint(user_management_route,
                           url_prefix="/api/v1/users")
    app.register_blueprint(food_management_route,
                           url_prefix="/api/v1/foods")
    app.register_blueprint(restaurant_management_route,
                           url_prefix="/api/v1/restaurant")

    return app
