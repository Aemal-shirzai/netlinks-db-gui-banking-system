from connections import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(app, db) # flask migrate
manager = Manager(app) # for scripting
manager.add_command('db', MigrateCommand)


class Admin(db.Model):
    """This Class is migration for admins table.
    
    it contains table name, id, name, email, password and is_supper columns
    """
    __tablename__ = 'admins'
    id = db.Column (db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_supper = db.Column(db.Boolean(), nullable=False, default=False)


class User(db.Model):
    """This Class is migration for admins table.
    
    it contains table name, id, name,addres, balance email and password columns
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Integer, nullable=False, default='0', server_default='0')
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    
if __name__ == '__main__':
    manager.run()
