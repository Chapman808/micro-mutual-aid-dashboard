from wtforms import SubmitField, TextAreaField, SelectField
from flask_wtf import FlaskForm 


class ProfileForm(FlaskForm):
  name = SelectField('Name', choices=('Eva', 'Zubee'))
  needs = TextAreaField('What I might need')
  provides = TextAreaField('What I might like to give')

  submit = SubmitField('Generate')