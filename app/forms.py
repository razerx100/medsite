from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    password_re = PasswordField("Re Enter Password", [DataRequired()])
    email = StringField("Email", [DataRequired()])
    register = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", [DataRequired()])
    password = PasswordField("Password", [DataRequired()])
    remember_me = BooleanField("Remember me")
    login = SubmitField("Login")
