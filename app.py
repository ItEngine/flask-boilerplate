from flask import Flask, render_template
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.main.controllers import main

# App flask
app = Flask(__name__)
# Config flask
app.config.from_object('config')
# Config admin
admin = Admin(app, name='Admin', template_mode='bootstrap3')

# Config SQLAlchemy and migrations
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import module main
app.register_blueprint(main, url_prefix='/')

if __name__ == "__main__":
    app.run()
