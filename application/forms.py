from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.model import User

class LoginForm(FlaskForm):
    email       = StringField(label="Email", validators=[DataRequired(), Email()])
    password    = StringField(label="Password", validators=[DataRequired(), Length(min=6, max=20)])
    remember_me = BooleanField(label="Remember me")
    submit      = SubmitField(label="Login")


class RegisterForm(FlaskForm):
    email               = StringField(label="Email", validators=[DataRequired()])
    password            = StringField(label="Password", validators=[DataRequired(), Length(min=6, max=20)])
    password_confirmed  = StringField(label="Confirm Password", validators=[DataRequired(),
                            Length(min=6, max=20), EqualTo('password')])
    first_name          = StringField(label="First name", validators=[DataRequired(),
                            Length(min=3, max=80)])
    last_name           = StringField(label="Last name", validators=[DataRequired(),
                            Length(min=3, max=80)])    
    submit              = SubmitField(label="Register Now")

    def validate_email(self, email):
        # cannot occur more than once because email is unique set in the model
        user = User.objects(email=email.data).first()
        if user: 
            raise ValidationError("email is already in use, pick another one")
 
