from models.user_model import Roles, UserRoles


class RolesRepo:

    @staticmethod
    def get_role(role_name):
        """
            Get Role
        """
        role_data = Roles.query.filter(
            Roles.role_name == role_name).first()
        return role_data
