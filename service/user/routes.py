from flask import Blueprint
# from flask_user import ro
from common.session import get_current_user_id
from service.forms.user_management_forms import SignupForm, LoginForm, OwnerSignupForm, AgentSignupForm, VerifyCodeForm
from service.user.views import UserData, MFA

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


@user_management_route.route("/signup/delivery-agent", methods=["PUT"])
def delivery_agent_signup():
    form = AgentSignupForm()
    response = UserData.delivery_agent(form)
    return response


@user_management_route.route("/login", methods=["POST"])
def login():
    form = LoginForm()
    response = UserData.user_login(form)
    return response


@user_management_route.route("/get-user", methods=["GET"])
def get_user():
    user_id = get_current_user_id()
    return user_id


@user_management_route.route("/mfa/verify", methods=["POST"])
def verify_mfa():
    form = VerifyCodeForm()
    response = MFA.verify_mfa(form)
    return response
