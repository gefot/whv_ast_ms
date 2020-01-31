# app.py

### Working code
# import os
# from flask import Flask, render_template, session, redirect, url_for, flash
#
# from whv_ast_ms.forms import SignupForm, RecordingsForm
# from modules import functions
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'mysecretkey'

from whv_ast_ms.forms import SignupForm, RecordingsForm
from modules import functions

from whv_ast_ms import app, db
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from whv_ast_ms.models import User
from whv_ast_ms.forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome_user.html')




### Working Code
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = SignupForm()
#     if form.validate_on_submit():
#         session['login_username'] = form.login_username.data
#         session['login_password'] = form.login_password.data
#
#         if session['login_username'] != "whitehat" or session['login_password'] != "wh!teh@t":
#             flash('Wrong username or password')
#         else:
#             return redirect(url_for('main'))
#
#     return render_template('signup.html', form=form)
#
#
# @app.route('/main')
# def main():
#     return render_template('main.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/show_configured_users.html')
def show_configured_users():
    users = functions.get_configured_users()
    num_of_users = len(users)

    for user in users:
        print(user)

    return render_template('management/show_configured_users.html', users=users, num_of_users=num_of_users)


@app.route('/show_recordings.html', methods=['GET', 'POST'])
def show_recordings():
    form = RecordingsForm()

    # Dual purpose variable (Boolean/String); it is False if "Submit" was not clicked.
    date = False

    record_list = []
    record_list_len = 0

    if form.validate_on_submit():
        # session['data'] = form.date.data
        # session['agent'] = form.agent.data
        date = form.date.data
        print(type(date), date)

        if date is not "":
            record_list = functions.get_recordings(date)
            record_list_len = len(record_list)
            for record in record_list:
                print(record)
            # print(record_list)
            # print(record_list_len)

    return render_template('management/show_recordings.html', form=form, date=date, record_list=record_list, record_list_len=record_list_len)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
