from flask import Blueprint, session, jsonify

from common.rbac import has_permission
from common.role_constant import Roles
from common.session import get_current_user_id
from service.forms.food_management_forms import MenuForm
from service.food.views import FoodData

food_management_route = Blueprint("food_management_route", __name__)

@food_management_route.route("/add_menu", methods=["PUT"])
def add_menu():
    form = MenuForm()
    response = FoodData.add_menu(form)
    return response
