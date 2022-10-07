import pyotp
from query.role_query import RolesRepo
from common.constant import INVALID_FORM_MESSAGE
from common.mfa_secret import decrypt_mfa_secret, send_mfa, encrypt_mfa_secret
from exception.http_exception import HttpException
from service.user.query.user_query import UserRepo
from flask import jsonify, Flask, request
from common.password_converter import generate_password_hash
from common.jwt_token import generate_jwt_token, decode_jwt_token
from common import constant, role_constant
from common.session import get_current_user_id, create_session

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class UserData:

    @staticmethod
    def user_signup(form):
        # if not form.validate_on_submit():
        #     raise HttpException(INVALID_FORM_MESSAGE, 400)
        user_data = list()
        email = form.email.data
        user = UserRepo.get_user_details(email)

        # check if user exists
        if user:
            return jsonify('User already exist', 403)

        # Generating mfa-secret-key  & temporary JWT token
        raw_mfa_secret = pyotp.random_base32()

        # generate=ing temporary JWT token
        token = generate_jwt_token(
            email, constant.TEMPORARY_JWT_EXP_TIME_MINS)

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
            'mfa_secret': encrypt_mfa_secret(raw_mfa_secret),
        }
        role_data = RolesRepo.get_role(role_constant.Roles.USER_PERMISSION)

        user_data.append(data)
        UserRepo.create_user(user_data)

        # if data.get('is_owner'):
        #     UserData.owner_user()
        data = {key: data[key] for key in data if key not in ['password_hash','mfa_secret']}
        return jsonify(
            {'message': 'success',
             "jwt_token": {
                 "token": token.decode("utf-8"),
                 "exp_time_in_minutes": constant.TEMPORARY_JWT_EXP_TIME_MINS,
             },
             'data': data

             })

    @staticmethod
    def user_login(form):
        email = form.email.data
        password = form.password.data

        user = UserRepo.get_user_details(email=email)
        if not user:
            return jsonify('User does not exist', 403)
        token = generate_jwt_token(
            email, constant.TEMPORARY_JWT_EXP_TIME_MINS)
        entered_password_hash = generate_password_hash(
            password).encode("utf-8")
        if entered_password_hash != user.password_hash:
            return jsonify('Incorrect password', 403)
        mfa_secret = decrypt_mfa_secret(user.mfa_secret)
        response_payload = {
            "jwt_token": {
                "token": token.decode("utf-8"),
                "exp_time_in_minutes": constant.
                TEMPORARY_JWT_EXP_TIME_MINS,
                "mfa_code": send_mfa(mfa_secret)
            }
        }
        return {'message': 'login success', 'token': response_payload}

    @staticmethod
    def owner_user(form):
        # if not form.validate_on_submit():
        #     raise HttpException(INVALID_FORM_MESSAGE, 400)
        owner_data = list()
        restaurant_email = form.email.data
        fssai_number = form.fssai_number.data

        owner = UserRepo.get_owner_details(fssai_number)
        # check if user exists
        if owner:
            return jsonify('User already exist', 403)

        data = {
            'restaurant_name': form.restaurant_name.data,
            'restaurant_address': form.restaurant_address.data,
            'restaurant_contact': form.restaurant_contact.data,
            'restaurant_email': restaurant_email,
            'fssai_number': fssai_number,
            'gst_number': form.gst_number.data,
            'establishment_type': form.establishment_type.data,
            'outlet_type': form.outlet_type.data,
            'is_owner': True

        }
        owner_data.append(data)
        UserRepo.create_user(owner_data, data.get('is_owner'))

        return {'message': 'Owner details logged in successfully', 'data': data}

    @staticmethod
    def delivery_agent(form):
        # if not form.validate_on_submit():
        #     raise HttpException(INVALID_FORM_MESSAGE, 400)
        agent_data = list()
        aadhar_card_number = form.aadhar_card_number.data

        agent = UserRepo.get_agent_details(aadhar_card_number)
        # check if user exists
        if agent:
            return jsonify('User already exist', 403)

        data = {
            'vehicle_type': form.vehicle_type.data,
            'driving_licence_number': form.driving_licence_number.data,
            'aadhar_card_number': aadhar_card_number,
            'vehicle_number': form.vehicle_number.data,
            'job_type': form.job_type.data,
            'is_delivery_agent': True
        }
        agent_data.append(data)
        UserRepo.create_user(agent_data, data.get('is_delivery_agent'))

        return {'message': 'Agent details logged in successfully', 'data': data}


class MFA:
    @staticmethod
    def verify_mfa(form):
        if not form.validate_on_submit():
            raise HttpException(INVALID_FORM_MESSAGE,
                                constant.BAD_REQUEST_CODE, 400)
        email = form.email.data
        mfa_code = form.code.data

        user_data = UserRepo.get_user_details(email=email)
        if not user_data:
            raise HttpException(constant.USER_DOES_NOT_EXIST,
                                constant.UNAUTHORISED, 401)

        if user_data.mfa_secret:
            mfa_secret = decrypt_mfa_secret(user_data.mfa_secret)
        else:
            raise HttpException(constant.NO_INVITATION,
                                constant.UNAUTHORISED, 401)

        headers = request.headers
        bearer = headers.get('Authorization')  # Bearer YourTokenHere
        token = bearer.split()[1]

        token = token.encode(constant.UTF_ENCODING)
        decoded = decode_jwt_token(token)

        if decoded["email"] == user_data.email:
            totp = pyotp.TOTP(
                mfa_secret, interval=constant.MFA_TIME_INTERVAL)
            if totp.verify(mfa_code):
                jwt_payload = {
                    'email': user_data.email,
                    'name': user_data.name,
                    'contact_number': user_data.contact_number,
                    'address': user_data.address,
                    'city': user_data.city,
                    'state': user_data.state,
                    'zip_code': user_data.zip_code,
                    'user_id': user_data.user_id
                }
                jwt_token = generate_jwt_token(user_data.email,
                                               constant.TEMPORARY_JWT_EXP_TIME_MINS, jwt_payload=jwt_payload)
                create_session(jwt_token)
                user_id = get_current_user_id()

                response = {
                    "code": constant.SUCCESS_CODE,
                    "message": constant.CODE_VERIFIED_SUCCESSFULLY,
                    "user_data": {
                        'email': user_data.email,
                        'name': user_data.name,
                        'contact_number': user_data.contact_number,
                        'address': user_data.address,
                        'user_id': user_id
                    }
                }
                return jsonify(response, 200)
        else:
            raise HttpException(constant.INVALID_JWT_TOKEN,
                                constant.UNAUTHORISED, 401)
