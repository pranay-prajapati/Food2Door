from flask_wtf import FlaskForm
import wtforms_json
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email

wtforms_json.init()


class MenuForm(FlaskForm):
    dish_name = StringField(validators=[DataRequired()])
    price = StringField(validators=[DataRequired()])
    ingredients = StringField()
    is_customisable = BooleanField()
