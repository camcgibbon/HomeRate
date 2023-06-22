from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LocationForm(FlaskForm):
    location = StringField('location', validators=[DataRequired()])
    submit = SubmitField('Submit')