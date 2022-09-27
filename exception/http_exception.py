from common.constant import DEFAULT_HTTP_ERROR_MESSAGE, DEFAULT_ERROR_CODE, DEFAULT_HTTP_ERROR_CODE


class HttpException(Exception):
    def __init__(self, message=DEFAULT_HTTP_ERROR_MESSAGE, code=DEFAULT_ERROR_CODE, http_code=DEFAULT_HTTP_ERROR_CODE):
        self.code = code
        self.message = message
        self.http_code = http_code
        super().__init__(message)
