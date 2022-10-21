from flask import Blueprint, session, jsonify, request

from common.rbac import has_permission
from common.role_constant import Roles
from common.session import get_current_user_id
from service.forms.food_management_forms import MenuForm
from service.food.views import FoodData
from common.role_constant import Roles

food_management_route = Blueprint("food_management_route", __name__)


@food_management_route.route("/add-menu", methods=["PUT"])
@has_permission(permissions=Roles.RESTAURANT_PERMISSION)
def add_menu():
    form = MenuForm()
    response = FoodData.add_menu(form)
    return response


@food_management_route.route("/show-restaurant", methods=["GET"])
def show_restaurant():
    response = FoodData.show_restaurant()
    return response


@food_management_route.route("/show-restaurant/<restaurant_id>/show-menu/", methods=["GET"])
def show_menu(restaurant_id):
    response = FoodData.show_menu(restaurant_id)
    return response


@food_management_route.route("/show-restaurant/<restaurant_id>/show-menu/<menu_id>/cart", methods=["POST"])
@has_permission(permissions=Roles.USER_PERMISSION)
def add_cart(restaurant_id, menu_id):
    cart_data = request.json
    response = FoodData.add_cart(restaurant_id, menu_id, cart_data)
    return response


@food_management_route.route("/show-restaurant/<restaurant_id>/show-menu/<menu_id>/cart/res/<cart_id>")
def restaurant_order_assignment(restaurant_id, menu_id, cart_id):
    response = FoodData.res_order_assignment(restaurant_id, menu_id, cart_id)
    return response


@food_management_route.route("/show-restaurant/<restaurant_id>/show-menu/<menu_id>/cart/agent/<cart_id>", methods=["POST"])
def agent_order_assignment(restaurant_id, menu_id, cart_id):
    response = FoodData.agent_order_assignment(restaurant_id, cart_id, menu_id)
    return response\


@food_management_route.route("/show-restaurant/<restaurant_id>/show-menu/<menu_id>/cart/user/<cart_id>/<agent_id>/<order_id>",
                             methods=["POST"])
def agent_order_acceptance(restaurant_id, menu_id, cart_id, agent_id, order_id):
    update = request.json if request.json else None

    response = FoodData.agent_order_acceptance(restaurant_id, cart_id, menu_id, agent_id, order_id, update)
    return response

# @food_management_route.route("/show-restaurant/<restaurant_id>/show-menu/<menu_id>/cart/user/<cart_id>/<agent_id>",
#                              methods=["POST"])


