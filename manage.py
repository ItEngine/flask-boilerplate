from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import app, db
from apps.main import models

# Configutation app
app.config.from_object('config')

# flask-migrate instance
migrate = Migrate(app, db)
# flask-script instance
manager = Manager(app)


# shell context
def _make_context():
    return dict(app=app, db=db, models=models)

# Managers commands
manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == '__main__':
    manager.run()
