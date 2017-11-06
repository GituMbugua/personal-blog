import unittest
from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role, Photo, Blog, Comment
from flask_migrate import Migrate, MigrateCommand

# create app instance 
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    '''
    run unittests
    '''
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity = 2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role, UserRole = UserRole, Photo = Photo, Blog = Blog, Comment = Comment)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()