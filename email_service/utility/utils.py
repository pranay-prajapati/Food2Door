from time import sleep
import pika
from common.rabbitmq_config import RabbitmqConfig

TEMPLATE_MAP = {
    'test_email': 'test_email.html',
    'welcome_email': 'welcome_user.html',
    'mfa_code_email': 'mfa_code.html',
    'notify_delivery_agent': 'notify_delivery_agent.html',
    'notify_restaurant': 'notify_restaurant.html',
    'notify_customer': 'notify_customer.html',
    'picked_notification': 'picked_notification.html',
    'delivery_notification': 'delivery_notification.html',
}

SUBJECT_MAP = {
    'test_email': 'Test Email Notification',
    'welcome_email': 'Welcome to FooD2Door',
    'mfa_code': 'Your Code has been sent successfully ',
    'notify_agent': 'Request for Order Delivery',
    'notify_restaurant_team': 'Request for Order',
    'notify_customer': 'Order Update',
    'picked_notification': 'Order has been picked',
    'delivery_notification': 'Order has been delivered',
}


def get_subject_by_type(email_type: str):
    if email_type not in SUBJECT_MAP:
        print(f'Invalid email type is found : {email_type}')
    subject = SUBJECT_MAP.get(email_type)
    return subject


def get_template_path(request_type: str):
    if request_type not in TEMPLATE_MAP:
        print(f'No Templated is found for type : {request_type}')
    template_path = TEMPLATE_MAP.get(request_type)
    return template_path


def connect_to_rabbitmq():
    host = RabbitmqConfig.host
    port = RabbitmqConfig.port
    attempts = RabbitmqConfig.attempts
    delay = RabbitmqConfig.retry_delay_sec

    print(f"Connecting to rabbitmq server on {host}:{port}")
    for i in range(attempts):
        try:
            print(f" - attempt #{i}")
            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=host, port=port)
            )
            print(" - connected.")
            return connection
        except Exception as exc:
            print(f" - connection attempt failed: {exc}.\n"
                  "   waiting for {delay} seconds...")
            sleep(delay)
    raise RuntimeError(f"No RabbitMQ server found on {host}:{port}.")
