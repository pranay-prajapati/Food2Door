from models.food_management import Menu
from models.payment_management import Order
from models.user_model import User, Restaurant
from database.db_models import handler

db_session = handler.db_session


class FoodRepo:

    @staticmethod
    def add_menu(data):
        menu = list()
        for menu_data in data:
            menu.append(Menu(**menu_data))
        db_session.add_all(menu)
        db_session.commit()
        db_session.flush()

    @staticmethod
    def get_restaurant_data(user_id):
        res_data = Restaurant.query.filter(Restaurant.user_id_fk==user_id).first()
        return res_data

    @staticmethod
    def show_restaurant(location):
        res_data = Restaurant.query.filter_by(restaurant_city=location).all()
        return res_data

    @staticmethod
    def show_menu_by_restaurant_id(restaurant_id):
        menu_data = Menu.query.filter_by(restaurant_id_fk=restaurant_id).all()
        return menu_data

    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        res_data = Restaurant.query.filter_by(restaurant_id_fk=restaurant_id).first()
        return res_data


    @staticmethod
    def get_menu_details_by_id(menu_id):
        menu_data = Menu.query.filter_by(menu_id_fk=menu_id).all()
        return menu_data

    @staticmethod
    def add_cart(data):
        cart = list()
        for cart_data in data:
            cart.append(Order(**cart_data))
        db_session.add_all(cart)
        db_session.commit()
        db_session.flush()


