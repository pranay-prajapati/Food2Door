from constants.constant import INVALID_FORM_MESSAGE
from exception.http_exception import HttpException


class UserData:

    @staticmethod
    def user_signup(form):
        if not form.validate_on_submit():
            raise HttpException(INVALID_FORM_MESSAGE, 400)
        email = form.email.data
        password = form.password.data

        # check if user exists

        # create user


