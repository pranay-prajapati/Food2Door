from flask import Blueprint, session, jsonify, request

from common.rbac import has_permission
from common.role_constant import Roles
from common.session import get_current_user_id
from service.forms.user_management_forms import SignupForm, LoginForm, OwnerSignupForm, AgentSignupForm, VerifyCodeForm, \
    ResetPasswordForm
from service.user.views import UserData, MFA, Password, RestaurantOwner, DeliveryAgent

user_management_route = Blueprint("user_management_route", __name__)


@user_management_route.route("/signup", methods=["PUT"])
def signup():
    form = SignupForm()
    response = UserData.user_signup(form)
    return response


@user_management_route.route("/signup/owner", methods=["PUT"])
@has_permission(permissions=Roles.RESTAURANT_PERMISSION)
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
@has_permission(permissions=Roles.USER_PERMISSION)
def get_user():
    user_id = get_current_user_id()
    return user_id


@user_management_route.route("/mfa/verify", methods=["POST"])
def verify_mfa():
    form = VerifyCodeForm()
    response = MFA.verify_mfa(form)
    return response


@user_management_route.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return jsonify(message="User Logged Out")


@user_management_route.route("password/reset", methods=["POST"])
def reset_password():
    form = ResetPasswordForm()
    response = Password.reset_password(form)
    return response


@user_management_route.route("/profile-info", methods=["GET"])
def get_profile_details():
    response = UserData.get_details()
    return response


@user_management_route.route("/profile-info", methods=["PUT"])
def update_profile_details():
    request_data = request.json
    response = UserData.update_details(request_data)
    return response


@user_management_route.route("agent/show_order/<agent_id>", methods=["GET"])
@has_permission(permissions=Roles.DELIVERY_AGENT_PERMISSION)
def show_total_delivered_orders(agent_id):
    response = DeliveryAgent.show_total_delivered_orders(agent_id)
    return response


@user_management_route.route("/res/show_order/<restaurant_id>", methods=["GET"])
@has_permission(permissions=Roles.RESTAURANT_PERMISSION)
def show_order_restaurant(restaurant_id):
    response = RestaurantOwner.show_order_restaurant(restaurant_id)
    return response

@user_management_route.route("/user/show_order/", methods=["GET"])
@has_permission(permissions=Roles.USER_PERMISSION)
def show_user_order():
    user_id = get_current_user_id()
    response = UserData.show_user_order(user_id)
    return response
