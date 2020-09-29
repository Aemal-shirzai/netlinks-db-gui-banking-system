from connections import app, db
from passlib.hash import pbkdf2_sha256

class AdminModel(db.Model):
    """This Class represent the admins table in the database.
    
    Attributes:
    -----------
    __tablename__: str -- It stores the table name.
    id: integer -- It is admin unique id.
    name: str -- It is name of admin
    email: str -- Unique Email Address of Admin
    password: str -- Password for admin
    is_supper: boolean -- if the user is super admin or not

    Methods:
    __init__ : which is called when the class object is created.
    """
    __tablename__ = 'admins'
    id = db.Column (db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_supper = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, name, email, password, is_supper=False):
        self.name = name
        self.email = email
        self.password = pbkdf2_sha256.hash(password)
        self.is_supper = is_supper

class UserModel(db.Model):
    """This Class represent the admins table in the database.
    
    Attributes:
    -----------
    __tablename__: str -- It stores the table name.
    id: integer -- It is user unique id.
    name: str -- It is name of users
    address: str -- It is address of users
    balance: integer -- It is user account balance which is 0 at beginning
    email: str -- Unique Email Address of users
    password: str -- Password of user
    Methods:
    __init__ : which is called when the class object is created.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Integer, nullable=False, default='0', server_default='0')
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)   

    def __init__(self, name, address, email, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = pbkdf2_sha256.hash(password) 
        