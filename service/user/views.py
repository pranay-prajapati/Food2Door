from constants.constant import INVALID_FORM_MESSAGE
from exception.http_exception import HttpException
from service.user.query import UserRepo
from flask import jsonify
from constants import constant
from models.user_model import User


class UserData:

    @staticmethod
    def user_signup(form):
        if not form.validate_on_submit():
            raise HttpException(INVALID_FORM_MESSAGE, 400)
        email = form.email.data
        user = UserRepo.get_user_details(email)
        if user:
            return jsonify('User already exist', 403)

        password = form.password.data
        # data = {
        #     User.name: form.name.data,
        #     User.email: form.email.data,
        #     User.contact_number: form.contact_number.data,
        #     User.address: form.address.data,
        #     User.city: form.name.data,
        #     User.state: form.name.data,
        #     User.password_hash: form.password.data,
        #     User.zip_code: form.zip_code.data,
        # }
        # UserRepo.update_by(email, data)
        # return jsonify("success")
        # check if user exists

        # create user


