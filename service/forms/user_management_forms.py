from flask_wtf import FlaskForm
import wtforms_json
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email
from validators.custom_validators import PasswordValidator

wtforms_json.init()


class EmailForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])


class SignupForm(EmailForm):
    name = StringField(validators=[DataRequired()])
    contact_number = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    city = StringField(validators=[DataRequired()])
    state = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired(), PasswordValidator()])
    zip_code = StringField(validators=[DataRequired()])
    is_owner = BooleanField()
    is_delivery_agent = BooleanField()


class OwnerSignupForm(EmailForm):
    restaurant_name = StringField(validators=[DataRequired()])
    restaurant_address = StringField(validators=[DataRequired()])
    restaurant_contact = StringField(validators=[DataRequired()])
    fssai_number = StringField(validators=[DataRequired()])
    gst_number = StringField(validators=[DataRequired()])
    establishment_type = StringField(validators=[DataRequired()])
    outlet_type = StringField(validators=[DataRequired()])


class AgentSignupForm(EmailForm):
    vehicle_type = StringField(validators=[DataRequired()])
    driving_licence_number = StringField(validators=[DataRequired()])
    aadhar_card_number = StringField(validators=[DataRequired()])
    vehicle_number = StringField(validators=[DataRequired()])
    job_type = StringField(validators=[DataRequired()])


class LoginForm(EmailForm):
    password = StringField(validators=[DataRequired()])


class VerifyCodeForm(EmailForm):
    code = StringField(validators=[DataRequired()])
