from flask import Blueprint, request
from service.restaurant.views import RestaurantData

restaurant_management_route = Blueprint("restaurant_management_route", __name__)


@restaurant_management_route.route("/<restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    response = RestaurantData.fetch_restaurant_info(restaurant_id)
    return response


@restaurant_management_route.route("/<restaurant_id>", methods=["PUT"])
def update_restaurant_detail(restaurant_id):
    request_data = request.json
    response = RestaurantData.update_restaurant_info(request_data, restaurant_id)
    return response


@restaurant_management_route.route("/<restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    response = RestaurantData.remove_restaurant(restaurant_id)
    return response
