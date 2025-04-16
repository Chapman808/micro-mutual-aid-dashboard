from wtforms import SubmitField, TextAreaField
from flask_wtf import FlaskForm 


class ProfileForm(FlaskForm):
  expansions = TextAreaField('Profile')
  submit = SubmitField('Generate')