import json
from typing import Callable

import pika
from pika.spec import PERSISTENT_DELIVERY_MODE

from common import rabbitmq_config
from common.rabbitmq_config import Queues, RabbitmqConfig
from common.rabbitmq_exception import RabbitMQException


class RabbitMQService:

    def create_queue(
            self,
            channel:pika.channel.Channel,
            queue: Queues,
            callback: Callable[..., None]):
        """
        Create queue
        """
        channel.queue_declare(queue=queue.value, durable=True)
        channel.basic_qos(prefetch_count=1)

        channel.basic_consume(
            queue=queue.value,
            on_message_callback=callback,
            auto_ack=True
        )

    def send_msg_to_queue(
            self,
            message:str,
            queue: Queues,
            exchange: str = "",
            host: str = RabbitmqConfig.host,
            port: str = RabbitmqConfig.port):
        """
        Function to send one message to rabbit mq service
        """
        try:
            # create connection
            with pika.BlockingConnection(pika.ConnectionParameters(host=host, port=int(port))) as connection:
                print(f"Connecting to rabbitmq server on {host}:{port}")
                print(f"Message:{message} sending to queue:{queue}")
                channel = connection.channel()

                channel.basic_publish(
                    exchange=exchange,
                    routing_key=queue.value,
                    body=message,
                    properties=pika.BasicProperties(delivery_mode=PERSISTENT_DELIVERY_MODE))
                print("Closing connection.")

        except Exception as exc:
            error_message = f'Failed to connect to RabbitMQ service. Message wont be sent. \n Exception: {exc}'
            raise RabbitMQException(error_message) from exc

    def send_email_notification(self, body):
        self.send_msg_to_queue(
            message=json.dumps(body),
            queue=Queues.EMAIL_NOTIFICATION
        )


