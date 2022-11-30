from enum import Enum
from os import getenv

DEFAULT_EXCHANGE = ''


class Queues(Enum):
    EMAIL_NOTIFICATION = "email_notification"
    ORDER_QUEUE = "order_queue"


class RabbitmqConfig:
    host = getenv("RABBITMQ_HOST", "localhost")
    port = int(getenv("RABBITMQ_PORT", "5672"))
    attempts = 10
    retry_delay_sec = int(getenv("RABBITMQ_DELAY_RETRY_DELAY_SEC", "5"))
    ttl = int(getenv("RABBITMQ_TTL_SEC", "10000"))
    retry_count = int(getenv("RETRY_MAX_RETRY_COUNT", "3"))
    exchange = getenv("RABBITMQ_DEFAULT_EXCHANGE", 'amq.direct')
