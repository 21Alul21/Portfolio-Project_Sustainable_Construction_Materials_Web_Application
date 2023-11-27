
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField 
#from wtforms.validators import Length, DataRequired

class LoginForm(FlaskForm):

    username = StringField('username') #validators=[DataRequired(), Length(min=3, max=10)]
    password = PasswordField('password') #validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('submit')
