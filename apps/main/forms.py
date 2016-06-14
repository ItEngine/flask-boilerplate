from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from app import db
from apps.main import models


class LoginForm(Form):
    """
    Login form
    """
    username = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        if user.password != self.password.data:
            print("Entro")
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(models.User).filter_by(
            username=self.username.data).first()


class RegisterForm(Form):
    """
    Register form
    """
    name = TextField(
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


class ForgotForm(Form):
    """
    Forgot password form
    """
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
