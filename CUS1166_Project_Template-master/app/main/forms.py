from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField, TimeField
from wtforms.validators import ValidationError, DataRequired, Length


class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo', 'Todo'), ('doing', 'Doing'), ('done', 'Done')])
    submit = SubmitField('submit')


class AppointmentForm(FlaskForm):
    customer_name = StringField('Customers name', validators=[DataRequired()])
    appointment_title = StringField('Appointment Name', validators=[DataRequired()])
    appointment_date = DateField('Appointment Date', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])

    notes = StringField('Additional Notes')
    appointment_status_completed = SelectField('Status', choices=[('todo', 'Todo'), ('doing', 'Doing'), ('done', 'Done')])
    submit = SubmitField('Submit')
