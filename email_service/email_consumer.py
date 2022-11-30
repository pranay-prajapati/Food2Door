import json
import pathlib

from common.rabbitmq_consumer import BaseRabbitMQConsumer
from common.rabbitmq_services import RabbitMQService
from custom_exception import InvalidEmailMessageRequest
from email_config import SimpleMailProvider, EmailConfig, MailProvider
from utility import utils
from jinja2 import TemplateNotFound, FileSystemLoader, Environment

queue_service = RabbitMQService()


class EmailConsumerCallback(BaseRabbitMQConsumer):

    def __init__(self, provider: MailProvider):
        self.provider = provider
        absolute_path = pathlib.Path(__file__).parent.absolute()
        template_path = str(absolute_path) + "/templates/"

        template_loader = FileSystemLoader(searchpath=template_path)
        self.jinja_env = Environment(loader=template_loader, autoescape=True)

    @staticmethod
    def email_callback(channel, method, properties, body):
        callback_wrapper = EmailConsumerCallback(SimpleMailProvider())
        callback_wrapper.handle_callback(channel, method, properties, body)

    def process_message(self, channel, method, properties, body):
        print(body, "== body")
        body_object = json.loads(body)
        print(body_object, "========body object")
        value_map = body_object.get('value_map', {})
        print(value_map, "========value map")
        email_subject = body_object["value_map"].get('subject', None)
        print(email_subject, "========email subject")
        email_body = body_object #.get('body', None)
        print(email_body, "========email body")
        attachment_param = {}
        retry_count = body_object.get('retry_count', 0)

        try:
            email_address = body_object["email"]
            print(type(email_address), "====email add")
        except KeyError:
            raise InvalidEmailMessageRequest(
                'No Email Address found for sending mail.')

        if 'type' in body_object:
            email_type = body_object["type"]
            if not email_subject:
                subject = utils.get_subject_by_type(email_type)
                if value_map:
                    email_subject = subject.format(**value_map)

            template_path = utils.get_template_path(email_type)
            template = self.jinja_env.get_template(template_path)
            email_body = template.render(value_map)

        if email_subject and value_map:
            print(
                f'Sending Mail to : {email_address}')
            print(f"Email sending count {retry_count}")
            res = self.provider.send_mail(
                receiver=email_address,
                subject=email_subject,
                html_body=email_body,
                filename=body_object["type"],
                attachment_param=attachment_param,
                value_map=value_map
            )

            if not res:
                if retry_count < EmailConfig.MAX_RETRY_COUNT:
                    body_object['retry_count'] = retry_count + 1
                    queue_service.send_email_notification(body=body_object)
                else:
                    print(f'Max limit reached for retry sending email')
        else:
            raise InvalidEmailMessageRequest('Invalid Email Subject/Body is found, \n '
                                             f'hence skipping')

