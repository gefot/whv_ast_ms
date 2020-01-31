from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password ', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your e-mail has already been registered!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login!')


# This class is replaced by LoginForm class
class SignupForm(FlaskForm):
    login_username = StringField('Enter Username')
    login_password = PasswordField('Enter Password')
    submit = SubmitField('Login')


class RecordingsForm(FlaskForm):
    # date = wtforms.DateTimeField('Which date is your favorite?', format='%m/%d/%y', validators=[wtforms.validators.Required()])
    # start_date = wtforms.DateField('Start', validators=[wtforms.validators.Required()], format = '%d/%m/%Y', description = 'Time that the event will occur', widget=widgets.DatePickerWidget)
    # date = DateField('DatePicker', format='%Y%m%d')
    # print("In class:", date)

    date = StringField('Date of recording: ')
    # agent = wtforms.SelectField('Select Whitehat employee',
    #                             choices=[
    #                                 ('1011', 'William Griffith'),
    #                                 ('1012', 'Kim De Los Reyes'),
    #                                 ('1014', 'Daniel Drenski'),
    #                             ])
    submit = SubmitField('Submit')
