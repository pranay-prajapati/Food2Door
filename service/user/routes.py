from flask import Blueprint
from service.forms.user_management_forms import SignupForm
from service.user.views import UserData

user_management_route = Blueprint("user_management_route", __name__)


@user_management_route.route("/signup", methods=["PUT"])
def signup():
    form = SignupForm()
    response = UserData.user_signup(form)
    return response
