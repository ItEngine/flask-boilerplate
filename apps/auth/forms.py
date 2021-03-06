from flask import current_app

from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from apps.auth import models

db = current_app.db


class LoginForm(FlaskForm):
    """
    Login form
    """
    username = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

    def validate_login(self):
        user = self.get_user()
        if user is None:
            self.username.errors = ('Invalid username', )
            return False

        if not check_password_hash(user.password, self.password.data):
            self.password.errors = ('Invalid password', )
            return False

        if not user.is_active:
            self.username.errors = ('You are not an user active', )
            return False

        if not user.is_admin:
            self.username.errors = ('You are not an administrator', )
            return False

        return True

    def get_user(self):
        return db.session.query(models.User).filter_by(
            username=self.username.data).first()


class RegisterForm(FlaskForm):
    """
    Register form
    """
    first_name = TextField(
        'Name', validators=[DataRequired(), Length(min=6, max=25)]
    )
    last_name = TextField(
        'Surname', validators=[DataRequired(), Length(min=6, max=25)]
    )
    username = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )

    def validate_username(form, field):
        username = field.data
        user = db.session.query(models.User).filter_by(
            username=username
        ).first()

        if user is not None:
            raise ValidationError("The user is already registered")


class ForgotForm(FlaskForm):
    """
    Forgot password form
    """
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
