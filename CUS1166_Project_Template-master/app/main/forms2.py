
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, IntegerField, FloatField
from wtforms import RadioField
from wtforms.validators import DataRequired


class AppointmentForm(FlaskForm):
    name = StringField('appointment name', validators=[DataRequired()])
    start = DateTimeField('Start Date/Time', validators=[DataRequired()])
    end = DateTimeField('End Date/Time', validators=[DataRequired()])


    submit = SubmitField('Add Event')


class EventsPageForm(FlaskForm):
    appointment_id = IntegerField('appointment ID')
    submit = SubmitField('Attend')
