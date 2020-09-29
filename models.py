from connections import app, db
from passlib.hash import pbkdf2_sha256
from itsdangerous import TimedJSONWebSignatureSerializer as serializer


class AdminModel(db.Model):
    """This Class represent the admins table in the database.
    
    Attributes:
    -----------
    __tablename__: str -- It stores the table name.
    id: integer -- It is admin unique id.
    name: str -- It is name of adminpass
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

    def get_reset_token(self, expires=1800):
        '''This function create and get a new passwrod reset token for user'''
        s_obj = serializer(app.config["SECRET_KEY"], expires)
        token = s_obj.dumps({'user_id':self.id, 'utype':'admin'}).decode("utf-8")
        return token
    
    @staticmethod
    def verify_reset_token(token):
        '''This function verifies the token to be correct or not'''
        s_obj = serializer(app.config["SECRET_KEY"])
        try:
            # check if the we can get the user id and type from token or not
            user_id = s_obj.loads(token)['user_id']
            utype = s_obj.loads(token)['utype']
        except:
            # it means the token is not valid or expird if we dont get id from it
            return None
        data = {'user': AdminModel.query.get(user_id), 'user_type':utype}
        return data

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

    def get_reset_token(self, expires=1800):
        '''This function create and get a new passwrod reset token for user'''
        s_obj = serializer(app.config["SECRET_KEY"], expires)
        token = s_obj.dumps({'user_id':self.id,'utype':'user'}).decode("utf-8")
        return token
    
    @staticmethod
    def verify_reset_token(token):
        '''This function verifies the token to be correct or not'''
        s_obj = serializer(app.config["SECRET_KEY"])
        try:
             # check if the we can get the user id and type from token or not
            user_id = s_obj.loads(token)['user_id']
            utype = s_obj.loads(token)['utype']
        except:
            # it means the token is not valid or expird if we dont get id from it
            return None
        data = {'user': UserModel.query.get(user_id), 'user_type':utype}
        return data
    

    def __init__(self, name, address, email, password):
        self.name = name
        self.email = email
        self.address = address
        self.password = pbkdf2_sha256.hash(password) 
        
