from flask import Flask, render_template, request, flash, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from connections import app
from forms import LoginForm
from models import UserModel, AdminModel

@app.route("/login", methods=["GET", 'POST'])
def login():
    """This function load the login page and login user to system.
    
    It can be accessed using two methods. If the methods is a GET method it
    return the login template but if its a POST method it login the user to 
    the system based on credentials.
    """

    # redirct if user is already authenticated
    if is_authenticated():
        if is_admin():
            return redirect(url_for('admin_manage_profile'))
        else:
            return redirect(url_for('index'))

    #form instantiation
    login_form = LoginForm()

    if request.method == 'GET':
        return render_template("authentication/login.html", form=login_form)
    elif request.method == 'POST':
        if login_form.validate():
            user = check_credentials(
                request.form['email'].lower(), request.form['password'],
                request.form['user_type']
            )
            if user:
                if int(request.form['user_type']) == 1:
                    set_login_session(user.id, False, False)
                    return redirect(url_for('index'))
                else:
                    set_login_session(user.id, True, user.is_supper)
                    return redirect(url_for('profile'))
            else:
                flash("Invalid Email or Password!", "loginError")
                return render_template("authentication/login.html", form=login_form)
        else:
            flash("Invalid Email or Password!", "loginError")
            return render_template("authentication/login.html", form=login_form)


@app.route('/logout')
def logout():
    """Logout User and redirect to the login page"""

    if not is_authenticated():
        return redirect(url_for('login'))
    
    if delete_login_session():
        return redirect(url_for('login'))
    else:
        return (request.referrer)


def check_credentials(email_add, password, utype):
    """This function check user credentials.
    
    parameters:
    ----------
    email_add: str -- user typed email
    password: str -- user typed password
    utype: str  -- user selected login type

    Return:
    ------
    False: if credential is wrong
    UserData : if the user data is good
    """
    if int(utype) == 1:
        user = UserModel.query.filter_by(email=email_add).first()
    else:
        user = AdminModel.query.filter_by(email=email_add).first()

    if user:
        password_check = pbkdf2_sha256.verify(password, user.password)
        if password_check:
            return user
    
        return False
    

def set_login_session(id, is_admin, is_supper):
    """This funcrion set session after logged in.
    
    Parameters:
    ----------
    id: int -- id of the user to be set in the session
    utype: boolean -- if admin its true if not its false
    is_supper: boolean -- if the admin is super admin its True else False
    """
    session['logged_in_id'] = id
    session['is_admin'] = is_admin
    session['is_supper'] = is_supper

    return True


def delete_login_session():
    """This function delete the logged in session"""
    if is_authenticated():
        session.pop('logged_in_id')
        session.pop('is_admin')
        session.pop("is_supper")
        return True
    return False


def current_user():
    """This function returns current user data.
    
    Return: 
    -------
    user: if user is avilible
    Fales: if user is not availibe
    """
    if 'logged_in_id' in session and 'is_admin' in session:
        uid = session['logged_in_id']
        if session['is_admin']:
            user = AdminModel.query.get(uid)
        else:
            user = UserModel.query.get(uid)
        return user
    else:
        return False


def is_authenticated():
    """This function shows if user is authenticated or not.
    
    Return: boolean
    """
    if "logged_in_id" in session:
        return True

    return False


def is_admin():
    """This function shows if user is admin or not.
    
    Return: boolean
    """
    if 'is_admin' in session:
        if session['is_admin']:
            return True
        else:
            return False

    return False
    

def is_supper():
    """This function shows if user is supper admin or not.
    
    Return: boolean
    """
    if 'is_supper' in session:
        if session['is_admin'] and session['is_supper']:
            return True
        else:
            return False

    return False
    