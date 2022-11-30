from common.rabbitmq_config import Queues
from common.rabbitmq_services import RabbitMQService
from email_consumer import EmailConsumerCallback
from utility import utils

queue_service = RabbitMQService()


def main():
    """This app is about handling messages from message delivery services (i.e. RabbitMQ)."""

    connection = utils.connect_to_rabbitmq()
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)

    # queue_service.create_retry_queue(
    #     channel=channel,
    #     queue=Queues.EMAIL_NOTIFICATION,
    #     callback=EmailConsumerCallback.email_callback
    # )

    queue_service.create_queue(channel=channel,
                               queue=Queues.EMAIL_NOTIFICATION,
                               callback=EmailConsumerCallback.email_callback)

    try:
        channel.start_consuming()
    except KeyboardInterrupt as ex:
        print(f' Keyboard interrupt {ex}')
    except Exception as exc:
        print(f'Exception Found : {exc}')
    finally:
        channel.stop_consuming()
        connection.close()

    print('Waiting for messages. To exit press CTRL+C')


if __name__ == "__main__":
    main()
