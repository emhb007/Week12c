from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add Actor')