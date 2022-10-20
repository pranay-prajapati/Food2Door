from flask import session
from common.config import Config
from exception.http_exception import HttpException
from common import constant
from common.jwt_token import decode_jwt_token


def create_session(jwt_token):
    """
    Storing session data
    """
    session["jwt_token"] = jwt_token


def get_session_data(session):
    """
    Extracting Session data from JWT payload
    """

    if "jwt_token" not in session.keys():
        raise HttpException(code=constant.BAD_REQUEST_CODE, http_code=401, message="User Not Logged In")
    jwt_token = session["jwt_token"]
    data = decode_jwt_token(jwt_token)
    return data


def get_current_user_id():
    session_data = get_session_data(session)
    user_id = session_data["jwt_payload"]["user_id"]
    return user_id


def get_current_user_data():
    session_data = get_session_data(session)
    user_data = session_data["jwt_payload"]["email"]
    return user_data


def get_current_user_permissions(session_data):
    list_of_permissions = session_data["jwt_payload"]["role_permissions"]
    compound_data = {
        k: [d.get(k) for d in list_of_permissions]
        for k in set().union(*list_of_permissions)
    }
    permissions = list(set(sum(compound_data["permissions"], [])))
    return permissions
