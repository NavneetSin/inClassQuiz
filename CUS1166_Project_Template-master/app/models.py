
#from flask import url_for
from app import db
from flask_sqlalchemy import SQLAlchemy

class add(db.Model):
    __tablename__ = 'add'
    id = db.Column(db.Integer, primary_key=True)



class delete(db.Model):
    __tablename__ = 'delete'
    id = db.Column(db.Integer, primary_key=True)

class edit(db.Model):
    __tablename__ = 'edit'
    id = db.Column(db.Integer, primary_key=True)

# class Attendappointment(db.Model):
#     __tablename__ = 'attend'
#     user_id = db.Column(db.Integer, db.ForeignKey('Customers.id'), primary_key=True)
#     appointment_id = db.Column(db.Integer, db.ForeignKey('Appointment.id'), primary_key=True)

# class Customers(db.Model):
#     __tablename__ = 'customer'
#     id = db.Column(db.Integer, primary_key=True)
#     address = db.Column(db.String)
#     name = db.Column(db.String)
#     notes = db.Column(db.String)
#     appointment = db.relationship('customers', secondary ='attend',back_populates= 'appointments' )
#

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    location = db.Column(db.String)
    attending_user = db.relationship('Customers', secondary='attend', back_populates="appointments")
    appointment_id = db.relationship('Appointment', secondary = 'customer', back_populates = '' )


class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))
