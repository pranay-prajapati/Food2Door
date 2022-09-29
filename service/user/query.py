from models.user_model import User
from database.db_models import handler

db_session = handler.db_session


class UserRepo:

    @staticmethod
    def get_user_details(email):

        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def update_by(email, data):
        user_data = User.query.filter(
            User.email == email).update(data)
        if user_data:
            handler.db_session.commit()
        return user_data

    @staticmethod
    def create_user(data):
        users = []

        for user_data in data:
            users.append(User(**user_data))
        db_session.add_all(users)
        db_session.commit()
        db_session.flush()
        # users = User(**data)
        # db_session.add(users)
        # db_session.commit()
        # return users