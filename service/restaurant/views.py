from flask import jsonify

from common import constant
from common.session import get_current_user_id
from service.food.query import FoodRepo
from service.restaurant.query import RestaurantRepo


class RestaurantData:

    @staticmethod
    def fetch_restaurant_info(restaurant_id):
        res_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        data = {
            "restaurant_name": res_data.restaurant_name,
            "restaurant_email": res_data.restaurant_email,
            "restaurant_contact": res_data.restaurant_contact,
            "restaurant_address": res_data.restaurant_address,
            "restaurant_city": res_data.restaurant_city,
            "restaurant_state": res_data.restaurant_state,
            "outlet_type": res_data.outlet_type.value,
            "is_closed": res_data.is_closed
        }
        return jsonify({
            "data": data,
            "message": "Restaurant detail fetched successfully",
            "code": constant.SUCCESS_CODE
        })

    @staticmethod
    def update_restaurant_info(request_data, restaurant_id):
        user_id = get_current_user_id()
        if user_id != FoodRepo.get_restaurant_by_id(restaurant_id).user_id_fk:
            return jsonify({
                "code": constant.FORBIDDEN_CODE,
                "message": "Login with registered restaurant owner to update details"
            })
        RestaurantRepo.update_restaurant_detail(user_id, restaurant_id, request_data)

        return jsonify({
            "code": constant.SUCCESS_CODE,
            "message": "Details updated successfully"
        })

    @staticmethod
    def remove_restaurant(restaurant_id):
        RestaurantRepo.del_restaurant(restaurant_id)
        return jsonify(message="Restaurant deleted successfully")
