from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from web import app, db

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

# Run the manager
if __name__ == '__main__':
    manager.run()
