from flask import Flask
from service.user.routes import user_management_route


def create_app():

    from user.routes import user_management_route

    app = Flask(__name__)

    # register blueprint
    app.register_blueprint(user_management_route,
                           url_prefix="/api/v1/users")

    return app
