from flask_migrate import MigrateCommand
from flask_script import Manager
from micro import create_app

app = create_app()
manager = Manager(app)

# Enable db migrations to be run via the command line
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
