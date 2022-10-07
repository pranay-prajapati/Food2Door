from models.user_model import User, Restaurant, DeliveryAgent
from database.db_models import handler

db_session = handler.db_session


class UserRepo:

    @staticmethod
    def get_user_details(email):

        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def get_owner_details(fssai_number):
        user = Restaurant.query.filter_by(fssai_number=fssai_number).first()
        return user

    @staticmethod
    def get_agent_details(aadhar_card_number):
        agent = DeliveryAgent.query.filter_by(aadhar_card_number=aadhar_card_number).first()
        return agent

    @staticmethod
    def update_by(email, data):
        user_data = User.query.filter(
            User.email == email).update(data)
        if user_data:
            handler.db_session.commit()
        return user_data

    @staticmethod
    def create_user(data, is_owner=None, is_delivery_agent=None):
        users = list()
        owner = list()
        agent = list()

        if is_owner:
            for owner_data in data:
                owner.append(Restaurant(**owner_data))
            db_session.add_all(owner)
        if is_delivery_agent:
            for agent_data in data:
                agent.append(DeliveryAgent(**agent_data))
            db_session.add_all(agent)
        else:
            for user_data in data:
                users.append(User(**user_data))
            db_session.add_all(users)

        db_session.commit()
        db_session.flush()

    @staticmethod
    def create_owner(data):
        owner = list()
        for owner_data in data:
            owner.append(Restaurant(**owner_data))
        db_session.add_all(owner)
        db_session.commit()
        db_session.flush()

    @staticmethod
    def create_agent(data):
        agent = list()
        for agent_data in data:
            agent.append(DeliveryAgent(**agent_data))
        db_session.add_all(agent)

        db_session.commit()
        db_session.flush()
