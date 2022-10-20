from models.food_management import Menu, Cart
from models.payment_management import Order
from models.user_model import User, Restaurant
from database.db_models import handler
from models.common_models import OrderStatus

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
        res_data = Restaurant.query.filter(Restaurant.user_id_fk == user_id).first()
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
        res_data = Restaurant.query.filter_by(restaurant_id=restaurant_id).first()
        return res_data

    @staticmethod
    def get_menu_details_by_id(menu_id):
        menu_data = Menu.query.filter_by(menu_id=menu_id).all()
        return menu_data

    @staticmethod
    def add_cart(data):
        cart = list()
        for cart_data in data:
            cart.append(Cart(**cart_data))
        db_session.add_all(cart)
        db_session.commit()
        db_session.flush()

    @staticmethod
    def order_acceptance(menu_id):
        data = {
            'is_accepted': True,
            'order_status': OrderStatus.placed.value
        }
        order = Order.query.filter_by(menu_id_fk=menu_id).update(data)
        db_session.commit()
        return bool(order)

    @staticmethod
    def order_preparing(menu_id):
        data = {
            'order_status': OrderStatus.baking.value
        }
        order = Order.query.filter_by(menu_id_fk=menu_id).update(data)
        db_session.commit()
        return bool(order)

    @staticmethod
    def get_cart_details(cart_id):
        cart_data = Cart.query.filter_by(cart_id=cart_id).first()
        return cart_data

    @staticmethod
    def update_cart_details(cart_id):
        cart_update = Cart.query.filter_by(cart_id=cart_id).update({'is_ordered': True})
        db_session.commit()
        return bool(cart_update)

    @staticmethod
    def add_order_details(data):
        order = list()
        for order_data in data:
            order.append(Order(**order_data))
        db_session.add_all(order)
        db_session.commit()
        db_session.flush()
        return True
        # order_update = Order.query.update(data)
        # db_session.commit()
        # return bool(order_update)

    @staticmethod
    def update_order_details(data,order_id=None):
        order_data = Order.query.filter_by(order_id=order_id).update(data)
        db_session.commit()
        return bool(order_data)
