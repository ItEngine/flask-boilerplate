from flask import Flask, render_template

from flask_admin import Admin
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from apps.main import controllers
from apps.main import models


# App flask
app = Flask(__name__)
# Config flask
app.config.from_object('config')
# Config admin
admin = Admin(app, name='Admin', template_mode='bootstrap3')

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

# Import module main
app.register_blueprint(controllers.main, url_prefix='/')


# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run()
