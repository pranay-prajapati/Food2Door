from models.user_model import Roles, UserRoles
from database.db_models import handler

db_session = handler.db_session


class RolesRepo:

    @staticmethod
    def get_role(role_name):
        """
            Get Role
        """
        role_data = Roles.query.filter(
            Roles.role_name == role_name).first()
        return role_data

    @staticmethod
    def add_role(data, user_id=None):
        data = {
            "role_id_fk": data.role_id,
            "user_id_fk": user_id if user_id else None
        }
        user_role_data = UserRoles(**data)
        db_session.add(user_role_data)
        db_session.commit()
        return True

    @staticmethod
    def fetch_user_roles(user_id):
        role_id_list = [data[0] for data in UserRoles.query.with_entities(UserRoles.role_id_fk).filter(
            UserRoles.user_id_fk == user_id).all()]
        roles = Roles.query.with_entities(
            Roles.role_id,
            Roles.role_name,
            Roles.role_display_name,
            Roles.resources,
        ).filter(Roles.role_id.in_(role_id_list)).all()
        return roles

    @staticmethod
    def fetch_assigned_roles(user_id):
        results = RolesRepo.fetch_user_roles(user_id=user_id)
        key_list = ["id", "role_name", "role_display_name", "permissions"]
        data = [dict(zip(key_list, result)) for result in results]
        return data
