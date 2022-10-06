from flask import jsonify, make_response
from common import constant


class HttpResponseHandler:
    """
    Common methods to handle http responses.
    """

    @staticmethod
    def build(message, http_code, custom_code, **kwargs):
        response_dict = {
            'code': custom_code,
            'message': message
        }
        response_dict.update(kwargs)
        return jsonify(response_dict), http_code

    @staticmethod
    def invalid_credentials(message="Invalid Credentials", **kwargs):
        return HttpResponseHandler \
            .build(message=message, http_code=constant.BAD_REQUEST_CODE,
                   custom_code=constant.UNAUTHORISED, **kwargs)

    @staticmethod
    def build_with_page(page, data, message="Success", **kwargs):
        response_dict = {
            'page': page["page_no"],
            'page_size': page["page_size"],
            'data': data,
            'total_records': page['total_records'],
            'code': constant.SUCCESS
        }
        response_dict.update(kwargs)
        return HttpResponseHandler.build(message=message, http_code=constant.SUCCESS_CODE,
                                         custom_code=constant.SUCCESS, **response_dict)

    @staticmethod
    def success(message="Success", **kwargs):
        response_dict = {
            'code': constant.SUCCESS,
            'message': message
        }
        response_dict.update(kwargs)
        return jsonify(response_dict), constant.SUCCESS_CODE

    @staticmethod
    def bad_request(message="Bad Request", **kwargs):
        response_dict = {
            'code': constant.BAD_REQUEST,
            'message': message
        }
        if kwargs:
            response_dict.update(kwargs)
        return jsonify(response_dict), constant.BAD_REQUEST_CODE

    @staticmethod
    def exist(message="Entity Already Exist", **kwargs):
        response_dict = {
            'code': constant.ENTITY_EXISTS,
            'message': message
        }
        if kwargs:
            response_dict.update(kwargs)
        return jsonify(response_dict), constant.BAD_REQUEST_CODE

    @staticmethod
    def invalid_request_entity(message="Entity Does not Exist"):
        return jsonify({
            'code': constant.NO_ENTITY_FOUND,
            'message': message
        }), constant.BAD_REQUEST_CODE

    # Deprecated for now. Use no_data method
    @staticmethod
    def empty_response(message="No Content"):
        return jsonify({
            'code': constant.NO_CONTENT,
            'message': message
        }), constant.SUCCESS_CODE

    @staticmethod
    def no_data(message="Entity Does not Exist"):
        return jsonify({
            'code': constant.NO_CONTENT,
            'message': message
        }), constant.NO_CONTENT_CODE

    @staticmethod
    def general_exception(message="Something went wrong"):
        return jsonify({
            'code': constant.DEFAULT_ERROR_CODE,
            'message': message
        }), constant.DEFAULT_HTTP_ERROR_CODE

    @staticmethod
    def not_found(message="Not Found"):
        return jsonify({
            'code': 4041,
            'message': message
        }), constant.NOT_FOUND

