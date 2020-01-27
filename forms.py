import flask_wtf
import wtforms


class SignupForm(flask_wtf.FlaskForm):
    login_username = wtforms.StringField('Enter Username')
    login_password = wtforms.PasswordField('Enter Password')
    submit = wtforms.SubmitField('Login')


class RecordingsForm(flask_wtf.FlaskForm):
    # date = wtforms.DateTimeField('Which date is your favorite?', format='%m/%d/%y', validators=[wtforms.validators.Required()])
    # start_date = wtforms.DateField('Start', validators=[wtforms.validators.Required()], format = '%d/%m/%Y', description = 'Time that the event will occur', widget=widgets.DatePickerWidget)
    # date = DateField('DatePicker', format='%Y%m%d')
    # print("In class:", date)

    date = wtforms.StringField('Date of recording: ')
    # agent = wtforms.SelectField('Select Whitehat employee',
    #                             choices=[
    #                                 ('1011', 'William Griffith'),
    #                                 ('1012', 'Kim De Los Reyes'),
    #                                 ('1014', 'Daniel Drenski'),
    #                             ])
    submit = wtforms.SubmitField('Submit')
