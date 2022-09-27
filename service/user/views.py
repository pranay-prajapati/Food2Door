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
        # if not form.validate_on_submit():
        #     raise HttpException(INVALID_FORM_MESSAGE, 400)
        email = form.email.data
        user = UserRepo.get_user_details(email)
        if user:
            return jsonify('User already exist', 403)

        data = {
            User.name: form.name.data,
            User.email: form.email.data,
            User.contact_number: form.contact_number.data,
            User.address: form.address.data,
            User.city: form.city.data,
            User.state: form.state.data,
            User.password_hash: generate_password_hash(form.password.data).encode(
                "utf-8"
            ),
            User.zip_code: form.zip_code.data,
            User.is_owner: form.is_owner.data,
            User.is_delivery_agent: form.is_delivery_agent.data,
        }
        print("csdsd", data)
        UserRepo.update_by(email, data)
        return {'message': 'success', 'data': data}
        # check if user exists
        #
        # create user


