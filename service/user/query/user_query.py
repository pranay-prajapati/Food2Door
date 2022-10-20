from sqlalchemy import and_, or_

from models.user_model import User, Restaurant, DeliveryAgent
from database.db_models import handler

db_session = handler.db_session


class UserRepo:

    @staticmethod
    def get_user_details(email=None, user_id=None):

        if email:
            user = User.query.filter_by(email=email).first()
        if user_id:
            user = User.query.filter_by(user_id=user_id).first()
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
        elif is_delivery_agent:
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

    @staticmethod
    def get_available_delivery_agent_by_location(restaurant_location):
        # agent = DeliveryAgent.query.join(DeliveryAgent, DeliveryAgent.user_id_fk == User.user_id).\
        #         filter(Restaurant.restaurant_city and User.city == restaurant_location).\
        #         filter(DeliveryAgent.is_available == True).all()
        # agent = DeliveryAgent.query.join(User, User.user_id == DeliveryAgent.user_id_fk
        #                                  ).join(Restaurant, Restaurant.user_id_fk == User.user_id
        #                                         ).filter(and_(User.is_delivery_agent == True,
        #                                                       )).all()
        # agent = DeliveryAgent.query.join(User, User.user_id == DeliveryAgent.user_id_fk
        #                                  ).join(Restaurant, Restaurant.user_id_fk == User.user_id
        #                                         ).filter(Restaurant.restaurant_city==restaurant_location).filter(
        #     DeliveryAgent.is_available == True).all()

        agent2 = DeliveryAgent.query.join(
            User, User.user_id == DeliveryAgent.user_id_fk
        ).filter(DeliveryAgent.is_available == True,
                 User.city == restaurant_location).all()

        # agent3 = DeliveryAgent.query.join(
        #     Restaurant, Restaurant.user_id_fk == DeliveryAgent.user_id_fk
        # ).filter(DeliveryAgent.is_available == True,
        #          Restaurant.restaurant_city == restaurant_location)
        return agent2
