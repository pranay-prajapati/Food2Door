from flask import jsonify, Flask, request
from exception.http_exception import HttpException
from common.constant import INVALID_FORM_MESSAGE
from common.session import get_current_user_id
from service.food.query import FoodRepo

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class FoodData:

    @staticmethod
    def add_menu(form):
        # if not form.validate_on_submit():
        #     raise HttpException(INVALID_FORM_MESSAGE, 400)

        restaurant_data = list()
        user_id = get_current_user_id()
        data = {
            'restaurant_id_fk': FoodRepo.get_restaurant_data(user_id).restaurant_id,
            'dish_name': form.dish_name.data,
            'price': form.price.data,
            'ingredients': form.ingredients.data if form.ingredients.data else None,
            'is_customisable': form.is_customisable.data if form.is_customisable.data else False
        }
        restaurant_data.append(data)
        FoodRepo.add_menu(restaurant_data)

        return jsonify({
            'data': data,
            'message': 'success'
        })