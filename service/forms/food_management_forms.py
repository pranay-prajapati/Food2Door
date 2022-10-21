from flask_wtf import FlaskForm
import wtforms_json
from wtforms import StringField, BooleanField, IntegerField, FieldList
from wtforms.validators import DataRequired, Email

wtforms_json.init()


# class MenuForm(FlaskForm):
#     dish_name = StringField(validators=[DataRequired()])
#     price = StringField(validators=[DataRequired()])
#     # ingredients = FieldList(StringField())
#     is_customisable = BooleanField()
