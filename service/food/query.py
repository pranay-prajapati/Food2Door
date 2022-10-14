from models.food_management import Menu
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
