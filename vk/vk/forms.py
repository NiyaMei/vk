from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class User_data(FlaskForm):
    email = StringField('Phone or email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Don't remember me")
    submit = SubmitField('Login')
    signup = SubmitField("Sign up")