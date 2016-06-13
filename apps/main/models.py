from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy


# Instance SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    """
    Model User
    """
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))