from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email       = StringField(label="Email", validators=[DataRequired()])
    password    = StringField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remember me")
    submit = SubmitField(label="Login")


class RegisterForm(FlaskForm):
    email       = StringField(label="Email", validators=[DataRequired()])
    password    = StringField(label="Password", validators=[DataRequired()])
    password_confirmed    = StringField(label="Confirm Password", validators=[DataRequired()])
    first_name    = StringField(label="First name", validators=[DataRequired()])
    last_name    = StringField(label="Last name", validators=[DataRequired()])    
    submit = SubmitField(label="Register Now")
