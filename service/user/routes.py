from flask import Blueprint
from service.forms.user_management_forms import SignupForm, LoginForm
from service.user.views import UserData

user_management_route = Blueprint("user_management_route", __name__)


@user_management_route.route("/signup", methods=["PUT"])
def signup():
    form = SignupForm()
    response = UserData.user_signup(form)
    return response


@user_management_route.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    response = UserData.user_login(form)
    return response
