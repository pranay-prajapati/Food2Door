from constants.constant import INVALID_FORM_MESSAGE
from exception.http_exception import HttpException
from query import UserRepo
from flask import jsonify
from constants import constant

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

        # check if user exists

        # create user


