
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, DataRequired, EqualTo, InputRequired

class LoginForm(FlaskForm):
    """ the login form class for validation and creating login form attributes """
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('submit')

class RegistrationForm(FlaskForm):
    """ the registration form class for validation and creating registration form variables """
    username = StringField(validators=[DataRequired(), Length(min=3, max=10)])
    email = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_again = PasswordField(validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField()
    submit = SubmitField()
    
                           
                