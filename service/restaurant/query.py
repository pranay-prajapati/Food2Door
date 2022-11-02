from database.db_models import handler
from models.user_model import Restaurant


class RestaurantRepo:

    @staticmethod
    def update_restaurant_detail(user_id, restaurant_id, data):
        res_data = Restaurant.query.filter(
            Restaurant.user_id_fk == user_id, Restaurant.restaurant_id == restaurant_id).update(data)
        if res_data:
            handler.db_session.commit()
        return res_data

    @staticmethod
    def del_restaurant(restaurant_id):
        data = {
            'is_deleted': True
        }
        query = Restaurant.query.filter(Restaurant.restaurant_id == restaurant_id).update(data)
        handler.db_session.commit()
        result = bool(query)
        return result
