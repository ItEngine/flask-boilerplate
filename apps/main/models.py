import datetime
from flask import Blueprint
from app import db


class User(db.Model):
    """
    Model User
    """
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    date_join = db.Column(db.DateTime, default=datetime.datetime.utcnow)
