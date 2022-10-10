from flask import session
from common.session import get_session_data, get_current_user_permissions
from common.constant import FORBIDDEN_CODE


def has_permission(permissions: list):
    def decorator(api_route):
        def wrapper(*args, **kwargs):
            session_data = get_session_data(session)
            session_permissions = get_current_user_permissions(session_data)
            allowed = set(session_permissions).issubset(set(permissions))
            if allowed:
                return api_route(*args, **kwargs)
            return {"code": FORBIDDEN_CODE, "message": "Permission Denied"}, 403
        wrapper.__name__ = api_route.__name__
        return wrapper
    return decorator
