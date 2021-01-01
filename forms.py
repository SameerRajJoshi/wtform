from wtforms import SubmitField, BooleanField, PasswordField, StringField, validators
from flask_wtf import Form

class RegForm(Form):
    name_first = StringField('First Name', [validators.DataRequired()])
    name_last = StringField('Last Name', [validators.DataRequired()])
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6, max=35)])
    confirm = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password', message='Password Must Match')])
    submit = SubmitField('Submit')

class Login(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Submit')