from flask import render_template, redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.main.forms2 import AppointmentForm
from app.models import Task
from app.models import *
from app import db
from flask_sqlalchemy import SQLAlchemy


@bp.route('/appointment/remove/<int:appointment_id>', methods=['GET', 'POST'])
def remove_appointment(appointment_id):
    # Query database, remove items
    Appointment.query.filter(Appointment.appointment_id == Appointment).delete()
    db.session.commit()

    return redirect(url_for('main.appointments'))


@bp.route('/appointment/edit/<int:appointment_id>', methods=['GET', 'POST'])
def edit_appointment(appointment_id):
    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.task_desc = form.task_desc.data
        current_appointment.task_status = form.task_status_completed.data

        db.session.add(current_appointment)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.appointments'))

    # get task for the database.
    current_task = Task.query.filter_by(appointment_id=appointment_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data = current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/appointments_edit_view.html", form=form, appointment_id=appointment_id)


@bp.route('/appointment/<int:sortby>/', methods=['GET', 'POST'])
def appointment_page(sortby):
    # sortby can be [0,1,2,3,4], representing sorting by:
    # ID/Start Time/Name/Price/Location Respectively
    current_user_id = 0
    current_user = Appointment.query.get(current_user_id)
    events_user_attend = current_user.events
    attend_form = AppointmentForm()
    if attend_form.is_submitted():
        print(attend_form.event_id.data)
        selected_event_to_attend = Appointment.query.get(attend_form.apointment_id.data)
        if not current_user.is_Attending(selected_event_to_attend):
            current_user.attend_event(selected_event_to_attend)
        else:
            current_user.unattend_event(selected_event_to_attend)


def add_appointment():
    appointment_form = AppointmentForm()
    if appointment_form.validate_on_submit():
        appointment = Appointment(name=appointment_form.name.data, start=appointment_form.start.data,
                                  end=appointment_form.end.data)
        db.session.add(appointment)
        db.session.commit()
        appointment.save_list_of_categories(appointment_form.Categories.data.split(','))

    return render_template('add_appointment.html', appointment_form=appointment_form)


@bp.route('/appointments', methods=['GET', 'POST'])
def list_appointment():
    form = AppointmentForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Appointment()
        new_task.task_desc = form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.appointments'))

    todo_list = db.session.query(Task).all()

    return render_template("main/appointments.html", todo_list=todo_list, form=form)

# @bp.route('/_page/daily/<int:year>/<int:month>/<int:currentDay>')
# def calendar_page_daily(year, month, currentDay):
#     if (month > 12 or month < 1):
#         return ("Oops, the month is out of range!")
#     # Initialize some useful variables:
#     current_user_id = 0
#     c = calendar.TextCalendar(calendar.SUNDAY) # Calendar object starting on Sunday
#     now = datetime.datetime.now()
#     event_list = Event.query.all()
#     month_name = calendar.month_name[month]
#     daylist = list(c.itermonthdays(year, month))
#     day_delta = datetime.timedelta(days=1)
#     # daylist is the list of numbers to put in each box of the calendar,
#     # where 0 is an empty box, and 1 is the 1st of the month, etc.
#     # example: [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 0, 0]
#
#     if (month == 1):
#         days_in_previous_month = calendar.monthrange(year-1, 12)[1]
#     else:
#         days_in_previous_month = calendar.monthrange(year, month-1)[1]
#
#     days_in_current_month = calendar.monthrange(year, month)[1]
#
#     event_list = [None]
