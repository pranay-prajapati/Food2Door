import smtplib
import os
from abc import ABC, abstractmethod
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, current_app, render_template
from flask_mail import Mail, Message
import pathlib
import jinja2
from email_service.utility import utils

absolute_path = (pathlib.Path(__file__).parent.absolute())
# msg = MIMEMultipart()
app = Flask(__name__)
mail = Mail(app)  # instantiate the mail class


class EmailConfig:
    MAIL_SERVER = app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    MAIL_PORT = app.config['MAIL_PORT'] = 465
    MAIL_USERNAME = app.config['MAIL_USERNAME'] = 'devansh.v@zymr.com'
    MAIL_PASSWORD = app.config['MAIL_PASSWORD'] = 'Dev1d@4ever'
    MAIL_USE_TLS = app.config['MAIL_USE_TLS'] = False
    MAIL_USE_SSL = app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    # smtp_user = os.getenv("SMTP_USER")
    # smtp_pass = os.getenv("SMTP_PASS")
    # smtp_server = os.getenv("SMTP_SERVER")
    # smtp_port = os.getenv("SMTP_PORT", "587")
    # sender_email = os.getenv("SENDER_EMAIL", "")
    # sender_name = os.getenv("SENDER_NAME", "Devansh")


# class MailProvider(ABC):
#     @abstractmethod
#     def send_email(
#             self,
#             message_id: str,
#             addressee: str,
#             subject: str,
#             html_body: str,
#             attachment_param: dict,
#             body: str,
#             cc_addressee: str = None):
#         raise NotImplementedError("Trying to call abstract method")


class SimpleMailProvider():
    def __init__(self):
        # self.provider = provider
        absolute_path = pathlib.Path(__file__).parent.parent.absolute()
        template_path = str(absolute_path) + "/templates"

        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        self.jinja_env = jinja2.Environment(loader=template_loader, autoescape=True)
        if EmailConfig and EmailConfig.MAIL_PASSWORD and EmailConfig.MAIL_SERVER:
            print('Initialized the Simple Mail Provider')
        else:
            print('Please configure the mandatory environment variables')

    # def send_email(
    #         self,
    #         message_id: str,
    #         addressee: str,
    #         subject: str,
    #         html_body: str,
    #         attachment_param: dict,
    #         body: str = "For legacy purposes only. If you see this - something went wrong.",
    #         cc_addressee: str = None):
    #
    #     # msg = EmailConfig.mail
    #     # msg["Subject"] = subject
    #     # msg["From"] = email_service.utils.formataddr(
    #     #     pair=(EmailConfig.sender_name, EmailConfig.sender_email))
    #     # msg["To"] = addressee
    #     # msg["Cc"] = cc_addressee
    #     msg = Message(subject,
    #                   sender="from@example.com",
    #                   recipients=["to@example.com"])
    #
    #
    #     if attachment_param:
    #         """
    #         Recording MIME type for PDF attachment for Scorecard
    #         if attachment is sent
    #         Downloading scorecard PDF from Azure blob storage
    #         and attaching with email_service as MIME Base
    #         """
    #         file_path = attachment_param["pdf_file_path"]
    #         part = MIMEBase("application", "octet-stream")
    #         with open(file_path, "rb") as file:
    #             part.set_payload(file.read())
    #             encoders.encode_base64(part)
    #             msg.attach(part)
    #             part.add_header(
    #                 "Content-Disposition",
    #                 'attachment; filename="%s"' % attachment_param["attachment_name"],
    #             )
    #
    #     else:
    #         plain_part = MIMEText(body, "plain")
    #         msg.attach(plain_part)
    #
    #     if html_body is not None:
    #         html_part = MIMEText(html_body, "html")
    #         msg.attach(html_part)
    #     mail_sent = False
    #     try:
    #         server = smtplib.SMTP(
    #             host=EmailConfig.smtp_server,
    #             port=int(EmailConfig.smtp_port))
    #         server.ehlo()
    #         server.starttls()
    #         server.login(
    #             user=EmailConfig.smtp_user,
    #             password=EmailConfig.smtp_pass)
    #         print("Validated SMTP Username and Password")
    #         toaddrs = addressee + ", " + cc_addressee if cc_addressee else addressee
    #         server.sendmail(
    #             from_addr=EmailConfig.sender_email,
    #             to_addrs=toaddrs,
    #             msg=msg.as_string())
    #         mail_sent = True
    #         print(f"Email sent for message_id: {message_id}")
    #     except Exception as exc:
    #         print(f'Exception Occurred while sending mail for message_id: {message_id}, exception: {exc}',
    #               exc_info=True)
    #     finally:
    #         if attachment_param:
    #             file_path = attachment_param["pdf_file_path"]
    #             if os.path.exists(file_path):
    #                 os.remove(file_path)
    #         if mail_sent:
    #             server.quit()
    #     return mail_sent
    @staticmethod
    def send_mail(
            subject: str,
            receiver: list,
            username: str = None,
            attachment_param: dict = None,
            html_body: str = None,
            filename=None,
            body: str = "For legacy purposes only. If you see this - something went wrong.",
            cc_addresses: str = None,
            bcc_addresses: str = None):

        absolute_path = pathlib.Path(__file__).parent.absolute()
        template_path = str(absolute_path) + "/templates"

        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        jinja_env = jinja2.Environment(loader=template_loader, autoescape=True)
        msg = Message(
            subject,
            sender=EmailConfig.MAIL_USERNAME,
            # html = render_template('welcome_user.html', username= username)
        )
        msg.recipients = receiver
        msg.body = body
        email_type = utils.TEMPLATE_MAP.get(f'{filename}')
        subject = utils.get_subject_by_type(email_type)
        value_map = {
            'username': username if username else False,
            'subject': subject
        }
        # msg.cc = cc_addresses if cc_addresses else False
        # msg.bcc = bcc_addresses if bcc_addresses else False
        template_pathh = template_path + '/' + utils.get_template_path(f'{filename}')
        template = jinja_env.get_template(email_type)
        email_body = template.render(**value_map)
        # ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(str(absolute_path / 'templates')))
        # template = ENV.get_template(f'{filename}')
        # email_body = template.render(username=username)
        # msg.html = render_template(f'{filename}', username=username)
        msg.html = email_body
        if attachment_param and filename:
            msg.attach(filename=filename)

        if html_body is not None:
            msg.attach(content_type=html_body)

        mail.send(msg)
        print("Email send successfully!!!!")
