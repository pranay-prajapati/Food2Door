from flask import Blueprint
from service.forms.user_management_forms import SignupForm, LoginForm, OwnerSignupForm, AgentSignupForm
from service.user.views import UserData

user_management_route = Blueprint("user_management_route", __name__)


@user_management_route.route("/signup", methods=["PUT"])
def signup():
    form = SignupForm()
    response = UserData.user_signup(form)
    return response


@user_management_route.route("/signup/owner", methods=["PUT"])
def owner_signup():
    form = OwnerSignupForm()
    response = UserData.owner_user(form)
    return response


# @user_management_route.route("/signup/delivery-agent", methods=["PUT"])
# def delivery_agent_signup():
#     form = AgentSignupForm()
#     response = UserData.delivery_agent(form)
#     return response


@user_management_route.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    response = UserData.user_login(form)
    return response
