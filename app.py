
from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)      # instantiate the SQLAlchemy class
crypt = Bcrypt(app)       #instatiate the Bcrypt class


with app.app_context():
    """ ensures database is created within the app context with the help of
        the 'with' context manager
    """

    class User(db.Model):
     """ class used to create the users table """
     __tablename__ = 'users'
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     user_name = db.Column(db.String(10), unique=False, nullable=False)
     email = db.Column(db.String(100), unique=False, nullable=False)
     password = db.Column(db.String(60), unique=False, nullable=False)
     image = db.Column(db.String(20), unique=False, nullable=False, default='default.jpg')
     post = db.relationship('Post', backref='author', lazy=True)

    class Post(db.Model):
     """ class used to create the users table """
     __tablename__ = 'posts'
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     user_name = db.Column(db.String(200), unique=False, nullable=False)
     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     post_content = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
     
     db.create_all()  # for creating the database with the two tables above
    


@app.route('/', strict_slashes=False)
def home():
       """ the view function for the landing page """
       return render_template('landing_page.html', title='landing page')


@app.route('/home', strict_slashes=False)
def index():
     """ the view function for the project home page """
     return render_template('home.html',  title='project home page')


@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login_form():
    """ the view function that handles the login logic """
    form = LoginForm()
    if form.validate_on_submit():
         flash('login succesful')
         return redirect(url_for('index'))
    return render_template('login_form.html', form=form,  title='login page')


@app.route('/registration', strict_slashes=False, methods=['GET', 'POST'])
def registration_form():
    """ the view function that handles the registration logic """
    form = RegistrationForm()
    if form.validate_on_submit():
         flash('Registration was successful')
         return redirect(url_for('index'))
    return render_template('registration_form.html', form=form,  title='registration page')


@app.route('/about_me', strict_slashes=False)
def about_me():
    """ the view function renders the about me page """
    return render_template('about_me.html', title='about me')


if __name__ == '__main__':
    app.run(debug=True)
