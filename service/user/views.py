from common.constant import INVALID_FORM_MESSAGE
from exception.http_exception import HttpException
from service.user.query import UserRepo
from flask import jsonify, Flask
from common import constant
from models.user_model import User
from common.password_converter import generate_password_hash

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False
class UserData:

    @staticmethod
    def user_signup(form):
        if not form.validate_on_submit():
            raise HttpException(INVALID_FORM_MESSAGE, 400)
        user_data = list()
        email = form.email.data
        user = UserRepo.get_user_details(email)

        # check if user exists
        if user:
            return jsonify('User already exist', 403)

        data = {
            'name': form.name.data,
            'email': email,
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
        # if data.get('is_owner'):
        #     UserData.owner_user()
        return {'message': 'success', 'data': {k: v for k, v in data.items() if k != 'password_hash'}}

    @staticmethod
    def user_login(form):
        email = form.email.data
        password = form.password.data

        user = UserRepo.get_user_details(email=email)
        if not user:
            return jsonify('User does not exist', 403)
        entered_password_hash = generate_password_hash(
            password).encode("utf-8")
        if entered_password_hash != user.password_hash:
            return jsonify('Incorrect password', 403)
        return {'message': 'login success'}

    @staticmethod
    def owner_user(form):
        if not form.validate_on_submit():
            raise HttpException(INVALID_FORM_MESSAGE, 400)
        owner_data = list()
        fssai_number = form.fssai_number.data
        owner = UserRepo.get_user_details(fssai_number)
        # check if user exists
        if owner:
            return jsonify('User already exist', 403)

        data = {
            'restaurant_name': form.restaurant_name.data,
            'restaurant_address': form.restaurant_address.data,
            'restaurant_contact': form.restaurant_contact.data,
            'fssai_number': fssai_number,
            'gst_number': form.gst_number.data,
            'establishment_type': form.establishment_type.data,
            'outlet_type': form.outlet_type.data,
        }
        owner_data.append(data)
        UserRepo.create_owner(owner_data)

        return {'message': 'Owner details logged in successfully', 'data': data}
