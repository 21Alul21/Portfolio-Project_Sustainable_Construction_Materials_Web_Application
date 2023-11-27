
from flask import Flask, render_template, url_for, flash
from forms import LoginForm 
import os


app = Flask(__name__)
from config.config import Config
app.config.from_object(Config)




@app.route('/', strict_slashes=False)
def home():
       return render_template('index.html')

@app.route('/home', strict_slashes=False)
def index():
    return render_template('home.html')

@app.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    # if form.validate_on_submit():
    flash('successful validation')
    return render_template('login_form.html', form=form)

@app.route('/registration', strict_slashes=False)
def registration_form():
    return render_template('registration_form.html')




if __name__ == '__main__':
    app.run(debug=True)
