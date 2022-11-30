from common.constant import DEFAULT_RABBITMQ_ERROR_MESSAGE, DEFAULT_ERROR_CODE, DEFAULT_HTTP_ERROR_CODE


class RabbitMQException(Exception):
    """
        RabbitMQ Exception
    """

    def __init__(self, message=DEFAULT_RABBITMQ_ERROR_MESSAGE, code=DEFAULT_ERROR_CODE, http_code=DEFAULT_HTTP_ERROR_CODE):
        """
            Class initialization
        """
        self.code = code
        self.message = message
        self.http_code = http_code
        super().__init__(message)
