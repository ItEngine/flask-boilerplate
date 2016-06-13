from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db


# Configutation app
app.config.from_object('config')

# flask-migrate instance  
migrate = Migrate(app, db)
# flask-script instance
manager = Manager(app)

# Managers commands
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
