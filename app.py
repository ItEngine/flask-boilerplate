import os
import sys

from flask import Flask, render_template

from flask_admin import Admin
from flask_cors import CORS
import flask_login
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from apps.main import controllers


# App flask
app = Flask(__name__)
# Config flask
app.config.from_object('conf.config')

# Config SQLAlchemy and migrations
db = SQLAlchemy(app)
db.init_app(app)
db.app = app

# Cors config
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)

# Config Api REST
api = Api(app)

# Flask login instance
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    from apps.main.models import User
    return User.query.get(int(id))


def load_admin():
    """
    Configuration admin
    """
    from apps.utils import MyAdminIndexView
    admin = Admin(
        app, name='Admin', index_view=MyAdminIndexView(),
        template_mode='bootstrap3', base_template='admin_master.html',
    )

    return admin

admin = load_admin()


def import_modules():
    """
    Import modules admin and controllers
    """
    from apps.main import admin

    # Import module main
    app.register_blueprint(controllers.main, url_prefix='/')


# Import modules necessarys
import_modules()


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
