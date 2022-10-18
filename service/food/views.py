from flask import jsonify, Flask, request
from exception.http_exception import HttpException
from common.constant import INVALID_FORM_MESSAGE
from common.session import get_current_user_id
from service.food.query import FoodRepo
from service.user.query.user_query import UserRepo

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

    @staticmethod
    def show_restaurant():
        user_data = UserRepo.get_user_details(user_id=get_current_user_id())
        data = FoodRepo.show_restaurant(user_data.city)
        res_list = list()
        for i in range(len(data)):
            restaurant_data = {
                'restaurant_id': data[i].restaurant_id,
                'restaurant_name': data[i].restaurant_name,
                'restaurant_address': data[i].restaurant_address,
                'restaurant_contact': data[i].restaurant_contact,
                'establishment_type': data[i].establishment_type.value,
                'outlet_type': data[i].outlet_type.value
            }
            res_list.append(restaurant_data)

        return jsonify(
            {'message': 'success',
             'data': res_list
             })

    @staticmethod
    def show_menu(restaurant_id):
        data = FoodRepo.show_menu_by_restaurant_id(restaurant_id)
        menu_list = list()
        for i in range(len(data)):
            menu_data = {
                'menu_id': data[i].menu_id,
                'dish_name': data[i].dish_name,
                'price': data[i].price,
                'food_image_path': data[i].food_image_path if data[i].food_image_path else None,
                'food_quantity': data[i].food_quantity if data[i].food_quantity else None,
                'is_customisable': data[i].is_customisable if data[i].is_customisable else False,
                'ingredients': data[i].ingredients

            }
            menu_list.append(menu_data)

        return jsonify(
            {'message': 'success',
             'data': menu_list
             })

    @staticmethod
    def add_cart(restaurant_id, menu_ids):

        menu_list = list()
        order_list = list()
        menu_ids.split(',').append(menu_list)

        user_id = get_current_user_id()
        restaurant_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        # user_data = UserRepo.get_user_details(user_id=user_id)
        #
        for i in menu_list:
            menu = FoodRepo.get_menu_details_by_id(int(menu_list[i]))
            order_data = {
                'user_id_fk': user_id,
                'restaurant_id': restaurant_data.restaurant_id,
                'menu_id_fk': menu.menu_id,
                'dish_name': menu.dish_name,
                'price': menu.price,
            }
            FoodData.order_assignment(order_data)
            order_data = {key: order_data[key] for key in order_data if key not in ['restaurant_id']}
            order_list.append(order_data)

        FoodRepo.add_cart(order_list)
        # data = FoodRepo.add_cart(restaurant_id, menu_id)

        return jsonify({
            'message': 'success'
        })

    @staticmethod
    def order_assignment(order_data):
        restaurant_data = FoodRepo.get_restaurant_by_id(order_data.get('restaurant_id'))
        if restaurant_data.is_closed:
            print('closed')

        menu_data = FoodRepo.get_menu_details_by_id(order_data.get('menu_id'))
        acceptance = FoodRepo.order_acceptance(menu_data.menu_id)
        if acceptance:
            print(f"your order accepted by {restaurant_data.restaurant_name}")
            preparing = FoodRepo.order_preparing(menu_data.menu_id)
            if preparing:
                print(f"your order is preparing by {restaurant_data.restaurant_name}")
            ##delivery agent code below this
        else:
            print("waiting for acceptance")
