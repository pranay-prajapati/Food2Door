from abc import abstractmethod


class BaseRabbitMQConsumer:

    @abstractmethod
    def process_message(self, channel, method, properties, body):
        """
            To process messages using callback (main logic)
        """

    # def handle_exception(self, channel, method, properties, body, ex):
    #     retry_ex = self.get_retriable_exception()
    #
    #     try:
    #         if type(ex) in retry_ex:
    #             queue = method.routing_key
    #             delay_routing_key = self.get_delay_routing_key(queue)
    #             failed_routing_key = self.get_failed_routing_key(queue)
    #             logging.info(
    #                 f' Excpetion is in retry. Retring for message {body}')
    #             headers = dict()
    #             if properties.headers and properties.headers.get('x-retry-count'):
    #                 headers['x-retry-count'] = properties.headers['x-retry-count'] + 1
    #             else:
    #                 headers['x-retry-count'] = 1
    #
    #             logging.info(
    #                 f' Header retry count for exception {headers} and Config default retry count {RabbitmqConfig.retry_count}')
    #             if headers['x-retry-count'] < RabbitmqConfig.retry_count:
    #                 logging.info(
    #                     f'Sending message {body} to delay queue.')
    #                 self.on_retry(channel, method, properties, body, ex)
    #                 self.publish_message(channel, body, headers, delay_routing_key)
    #
    #             else:
    #                 logging.info(
    #                     f'Sending message {body} to failing queue.')
    #                 self.on_fail(channel, method, properties, body, ex)
    #                 self.publish_message(channel, body, headers, failed_routing_key)
    #
    #     except Exception as exc:
    #         logging.error(
    #             f"Exception found in common handle exception {exc}", exc_info=True)

    def handle_callback(self, channel, method, properties, body):
        """
            Common Callback
        """
        # try:
        self.process_message(channel, method, properties, body)
        print("process --")
        # except Exception as ex:
        #     print(
        #         f"Exception found in handle callback {ex}")
            # self.handle_exception(channel, method, properties, body, ex)
        # finally:
        #     print(
        #         f'Sending ack with delivery tag {method.delivery_tag}')
        #     channel.basic_ack(delivery_tag=method.delivery_tag)

