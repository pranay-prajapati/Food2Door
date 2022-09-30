from common.constant import INVALID_FORM_MESSAGE
from exception.http_exception import HttpException
from service.user.query import UserRepo
from flask import jsonify
from common import constant
from models.user_model import User
from common.password_converter import generate_password_hash


class UserData:

    @staticmethod
    def user_signup(form):
        if not form.validate_on_submit():
            raise HttpException(INVALID_FORM_MESSAGE, 400)
        user_data = list()
        email = form.email.data
        user = UserRepo.get_user_details(email)
        if user:
            return jsonify('User already exist', 403)

        data = {
            'name': form.name.data,
            'email': form.email.data,
            'contact_number': form.contact_number.data,
            'address': form.address.data,
            'city': form.city.data,
            'state': form.state.data,
            'password_hash': generate_password_hash(form.password.data).encode(
                "utf-8"
            ),
            'zip_code': form.zip_code.data,
            'is_owner': form.is_owner.data,
            'is_delivery_agent': form.is_delivery_agent.data,
        }
        user_data.append(data)
        UserRepo.create_user(user_data)
        return {'message': 'success', 'data': {k: v for k, v in data.items() if k != 'password_hash'}}
