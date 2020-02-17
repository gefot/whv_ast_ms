# app.py
from whv_ast_ms import app, db
from flask import render_template, redirect, request, url_for, flash, abort, send_from_directory
from flask_login import login_user, logout_user, login_required

from whv_ast_ms.models import User
from whv_ast_ms.forms import RegistrationForm, LoginForm
from whv_ast_ms.forms import RecordingsForm

from modules import functions
from scripts import import_creds


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome_user.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are now logged out!")
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in Successfully!')

            my_next = request.args.get('next')

            if my_next is None or not my_next[0] == '/':
                my_next = url_for('home')

            return redirect(my_next)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash("Thanks for Registering")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/show_configured_users.html')
@login_required
def show_configured_users():
    ami_connector = functions.ast_ami_connect(import_creds.AMI_CREDS)
    users = functions.ast_ami_get_users(ami_connector)

    new_users = []
    for user in users:
        if 'p' not in user.username:
            new_users.append(user)

    num_of_new_users = len(new_users)

    for user in new_users:
        print(user)

    return render_template('management/show_configured_users.html', users=new_users, num_of_users=num_of_new_users)


@app.route('/recordings_folder/<path:filename>')
def get_recordings_folder(filename):
    return send_from_directory(app.config['RECORDINGS_FOLDER'], filename, as_attachment=True)


@app.route('/show_recordings.html', methods=['GET', 'POST'])
@login_required
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
            print("lala")
            record_list = functions.get_recordings(date)
            print("record_list")
            print("okok")
            record_list_len = len(record_list)
            for record in record_list:
                print(record)
            # print(record_list)
            # print(record_list_len)

    return render_template('management/show_recordings.html', form=form, date=date, record_list=record_list, record_list_len=record_list_len)


@app.route('/show_active_users.html')
@login_required
def show_active_users():
    ami_connector = functions.ast_ami_connect(import_creds.AMI_CREDS)
    users = functions.ast_ami_get_users(ami_connector)
    num_of_users = len(users)

    for user in users:
        print(user)

    return render_template('monitor/show_active_users.html', users=users, num_of_users=num_of_users)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
