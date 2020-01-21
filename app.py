from flask import Flask, render_template

# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
import flask_wtf
import wtforms

from modules import functions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


class RecordingsForm(flask_wtf.FlaskForm):
    # date = wtforms.CharField(label='Date (eg: 20190528)', required=False)
    date = wtforms.StringField('Date of recording: ')
    submit = wtforms.SubmitField('Submit')


@app.route('/')
def index():
    return render_template('flask_signup.html')


@app.route('/main')
def main():
    return render_template('main.html')


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
        date = form.date.data

        if date is not "":
            record_list = functions.get_recordings(date)
            record_list_len = len(record_list)
            # print(record_list)
            # print(record_list_len)

    return render_template('management/show_recordings.html', form=form, date=date, record_list=record_list, record_list_len=record_list_len)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
