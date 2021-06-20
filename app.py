from flask import Flask

from flask_cors import CORS
from flask_login import LoginManager
from flask_mail import Mail
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps import create_admin, create_errorhandler


# App flask
app = Flask(__name__)

# Config flask
app.config.from_object('conf.config')

with app.app_context():
    # CSRF protect
    csrf = CSRFProtect(app)

    # Config SQLAlchemy and migrations
    db = SQLAlchemy(app)
    db.init_app(app)
    db.app = app
    app.db = db

    # Cors config
    CORS(
        app, resources={r"/*": {"origins": "*"}},
        headers=['Content-Type', 'X-Requested-With', 'Authorization']
    )

    # Config Api REST
    api = Api(app, decorators=[csrf.exempt])
    app.api = api

    # Config email
    mail = Mail()
    mail.init_app(app)

    # Flask login instance
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Create admin
    admin = create_admin(app)
    app.admin = admin

    # Create error handlers
    create_errorhandler(app)

    from apps.auth import blueprint as auth_blueprint
    from apps.main import blueprint as main_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)


if __name__ == "__main__":
    app.run()
