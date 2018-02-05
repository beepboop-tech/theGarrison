# Imports for client
import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

# App config for login and DB
app.config['SECRET_KEY'] = 'helloworld'




# Initialise bootstrap and DB
Bootstrap(app)


def drinks_list():
    lst = [
        ['sex_on_the_beach', ['vodka', 'rum']],
        ['gin and tonic', ['gin', 'tonic']],
        ['vodka and coke', ['vodka', 'coke']]
    ]
    return lst

@app.route('/')
def index():
    return render_template('index.html', drink_list=drinks_list())




if __name__ == '__main__':
    app.run(host='0.0.0.0')
