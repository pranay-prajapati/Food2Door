from flask_wtf import FlaskForm
import wtforms_json
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email
from validators.custom_validators import PasswordValidator


class EmailForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])


class SignupForm(EmailForm):
    name = StringField(validators=[DataRequired()])
    contact_number = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    city = StringField(validators=[DataRequired()])
    state = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired(), PasswordValidator()])
    zip_code = StringField(validators=[DataRequired()])
    # is_owner = BooleanField(validators=[DataRequired()])
    # is_delivery_agent =  BooleanField(validators=[DataRequired()])