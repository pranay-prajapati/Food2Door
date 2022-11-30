from abc import ABC, abstractmethod

from flask import Flask
from flask_mail import Mail, Message
import pathlib
import jinja2
from email_service.utility import utils

absolute_path = (pathlib.Path(__file__).parent.absolute())
app = Flask(__name__)
mail = Mail(app)  # instantiate the mail class


class EmailConfig:
    MAIL_SERVER = app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    MAIL_PORT = app.config['MAIL_PORT'] = 465
    MAIL_USERNAME = app.config['MAIL_USERNAME'] = 'devansh.v@zymr.com'
    MAIL_PASSWORD = app.config['MAIL_PASSWORD'] = 'Dev1d@4ever'
    MAIL_USE_TLS = app.config['MAIL_USE_TLS'] = False
    MAIL_USE_SSL = app.config['MAIL_USE_SSL'] = True
    MAX_RETRY_COUNT = app.config['MAX_RETRY_COUNT'] = 2
    mail = Mail(app)


class MailProvider(ABC):
    @abstractmethod
    def send_mail(
            self,
            subject: str,
            receiver: list,
            value_map: dict = None,
            attachment_param: dict = None,
            html_body: str = None,
            filename=None,
            body: str = None,
            cc_addresses: str = None,
            bcc_addresses: str = None):
        raise NotImplementedError("Trying to call abstract method")


class SimpleMailProvider(MailProvider):
    def __init__(self):
        # absolute_path = pathlib.Path(__file__).parent.parent.absolute()
        # template_path = str(absolute_path) + "/templates"
        #
        # template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        # self.jinja_env = jinja2.Environment(loader=template_loader, autoescape=True)
        if EmailConfig and EmailConfig.MAIL_PASSWORD and EmailConfig.MAIL_SERVER:
            print('Initialized the Simple Mail Provider')
        else:
            print('Please configure the mandatory environment variables')

    def send_mail(
            self,
            subject: str,
            receiver: list,
            value_map: dict = None,
            attachment_param: dict = None,
            html_body: str = None,
            filename=None,
            body: str = "For legacy purposes only. If you see this - something went wrong.",
            cc_addresses: str = None,
            bcc_addresses: str = None):

        absolute_path = pathlib.Path(__file__).parent.absolute()
        template_path = str(absolute_path) + "/templates"
        print(type(attachment_param), "===========attached params")
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        jinja_env = jinja2.Environment(loader=template_loader, autoescape=True)
        email_type = utils.TEMPLATE_MAP.get(f'{filename}')
        msg = Message(
            subject,
            sender=EmailConfig.MAIL_USERNAME
        )
        msg.recipients = receiver
        print(type(msg.recipients), "=======receiver")
        msg.body = body if body else False
        print(msg.body, "======msg body")

        msg.cc = cc_addresses if cc_addresses else False
        msg.bcc = bcc_addresses if bcc_addresses else False
        template = jinja_env.get_template(email_type)
        if value_map:
            print("value map che")
            email_body = template.render(**value_map)
            msg.html = email_body
        if filename:
            print(filename, "file name che")
            msg.attach(filename=filename)

        if html_body is not None:
            print("html body che")
            msg.attach(content_type=html_body)

        mail.send(msg)
        print("Email send successfully!!!!")
