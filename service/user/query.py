from models.user_model import User
from database.db_models import handler

db_session = handler.db_session

class UserRepo:

    @staticmethod
    def get_user_details(email):

        user = User.query.filter_by(email=email).first()
        return user
