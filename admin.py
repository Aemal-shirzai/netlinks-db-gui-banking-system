from flask import Flask, render_template, request, flash, redirect, url_for
from passlib.hash import pbkdf2_sha256
from connections import app, db 
from forms import AdminRegisterForm, UserRegisterForm, AdminUpdateForm, \
    changePasswordForm, UserUpdateForm
from models import AdminModel, UserModel
from authentication import is_authenticated, is_admin, current_user, is_supper



@app.route("/admin/register", methods=['GET', 'POST'])
def register():
    """This function add new user.
    
    It can be accessed using two http methods. If the method is GET it ruturns
    the user registration form else it adds the user to database.
    """

    if not is_authenticated() or not is_admin():
        return redirect(url_for('login'))
        
    form = UserRegisterForm()
    if request.method == "GET":
        return render_template("admin/register.html", form = form)
    else:
        if form.validate():
            if not email_is_unique(UserModel, form.email.data, "add"):
                flash("email already taken", category="emailNotUnique")
                return render_template("admin/register.html", form = form)
            else: 
                user = UserModel(form.name.data, form.address.data, 
                    form.email.data.lower(), form.password.data)
                db.session.add(user)
                db.session.commit()
                flash("User Created", category="addSuccess")
                return redirect(url_for('register'))
        else:
            return render_template("admin/register.html", form = form)


@app.route("/admin/users")
def users():
    """This function load users and return users list template."""
    if not is_authenticated() or not is_admin():
        return redirect(url_for('login'))
    
    users = load_users_admins(UserModel)
    return render_template("admin/users.html", users=users)


@app.route("/admin/register_admin", methods=["GET", "POST"])
def register_admin():
    """This function load register admin page and add new admin.
    
    Return Page: if the request is get request
    Add new record: if the reqeuest if post request and form is validatad 
    """
    if not is_authenticated() or not is_admin() or not is_supper():
        return redirect(url_for('login'))

    form = AdminRegisterForm()
    if request.method == "GET":
        return render_template("admin/register_admin.html", form = form)
    else:
        if form.validate():
            if not email_is_unique(AdminModel, form.email.data, "add"):
                flash("email already taken", category="emailNotUnique")
                return render_template("admin/register_admin.html", form = form)
            else: 
                admin = AdminModel(form.name.data, form.email.data.lower(), 
                    form.password.data)
                db.session.add(admin)
                db.session.commit()
                flash("Admin Created", category="addSuccess")
                return redirect(url_for('register_admin'))
        else:
            return render_template("admin/register_admin.html", form = form)


@app.route("/admin/admins")
def admin_list():
    """This function load users and return users list template."""
    if not is_authenticated() or not is_admin():
        return redirect(url_for('login'))
    
    users = load_users_admins(AdminModel)
    return render_template("admin/admin_list.html", users=users)


@app.route("/admin/manage_profile", methods=["GET", "POST"])
def admin_manage_profile():
    """This function return edit form in get reques and update info in post."""
    
    if not is_authenticated() or not is_admin():
        return redirect(url_for('login'))

    form = AdminUpdateForm()
    pass_form = changePasswordForm()

    if request.method == "GET":
        form.name.data = current_user().name if current_user() else "" 
        form.email.data = current_user().email if current_user() else ""
        return render_template("admin/edit_profile_admin.html", form=form,
             pass_form=pass_form
        )
    else:
        if form.validate():
            if not email_is_unique(AdminModel, form.email.data, 'update'):
                flash("email already taken", category="emailNotUnique")
                return render_template("admin/edit_profile_admin.html", form=form,
                        pass_form=pass_form
                    )
            if verify_password(form.password_verify.data):
                user = current_user()
                user.name = form.name.data
                user.email = form.email.data.lower()
                db.session.commit()
                flash("Admin Updated", category="addSuccess")
                return redirect(url_for('admin_manage_profile'))
            else:
                flash("Invalid Password", category="passwordIncorrect")
                return render_template("admin/edit_profile_admin.html", form=form,
                        pass_form=pass_form
                    )
        else:
            return render_template("admin/edit_profile_admin.html", form=form,
                    pass_form=pass_form
                )


@app.route("/changepassword", methods=["POST"])
def change_password():
    """This function change both users and amins password.

    It is accessable by both users and admin that is why we first access the 
    is_admin() to check if it is an admin or not.
    """

    if not is_authenticated():
        return redirect(url_for('login'))

    admin = is_admin()
    form = AdminUpdateForm() if admin else UserUpdateForm()
    pass_form = changePasswordForm()
    redirect_page_url = "admin/edit_profile_admin.html" if admin \
            else "edit_profile.html"
    redirect_url = "admin_manage_profile" if admin else "profile"

    user = current_user()
    if pass_form.validate():
        if not verify_password(pass_form.old_password.data):
            flash("Invalid Password", category="old_pass_incorect")
            return render_template(redirect_page_url, form=form,
                    pass_form=pass_form
                )
        else:
            user.password = pbkdf2_sha256.hash(pass_form.new_password.data)
            db.session.commit()
            flash("Password Changed", category="addSuccess")
            return redirect(url_for(redirect_url))
    else:
        return render_template(redirect_page_url, form=form,
                pass_form=pass_form
            )


def email_is_unique(model, email, ftype):
    """This function query the table to check the email is unique or not.
    It is shared by both users and admins. for admins when they add new user 
    or another admin. And for users when the update their profile info.
    
    parameters:
    ----------
    model: model -- The model in whihc it has to search form
    email: str -- The value of email to be checked
    ftype: string -- Specify it checks for update or adding

    Return: boolean
    """
    if not is_authenticated():
            return redirect(url_for('login'))
    
    if ftype == 'add':
        row = model.query.filter_by(email=email).first()
    else:
        # now check email to be unique in all rows except the current one
        rows = model.query.filter_by(email=email).all()
        for row in rows:
            if row.id != current_user().id:
                return False
        row = None

    if row is not None:
        return False
    else:
        return True
        

def verify_password(password):
    """This function check the user password by hashing them
    
    parameters:
    ----------
    password: the user typed password

    Return: Boolean
    """
    if not is_authenticated():
        return redirect(url_for('login'))
    user = current_user()
    result = pbkdf2_sha256.verify(password, user.password)
    return result


def load_users_admins(model):
    """This function loads all users and admins.
    
    parameters:
    ----------
    model: using this paramenter this function decides which category of users
        to load. Admins or normal users.
    
    Return: model object
    """
    data = model.query.all()
    return data


@app.route('/admin/delete_users', methods=["POST"])
def delete_users():
    """This function delete users"""
    if not is_authenticated() or not is_admin():
        return redirect(url_for('login'))
        
    id = request.form.get("id")
    user = UserModel.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash("Recored Deleted", category="addSuccess")
    return redirect(request.referrer)


@app.route('/admin/delete_admins', methods=["POST"])
def delete_admins():
    """This function delete admiins. only by super admins. """
    if not is_authenticated() or not is_admin() or not is_supper():
        return redirect(url_for('admin_list'))
    
    id = request.form.get("id")
    user = AdminModel.query.get(id)
    if user.is_supper:
        return redirect(request.referrer)

    db.session.delete(user)
    db.session.commit()
    flash("Recored Deleted", category="addSuccess")
    return redirect(request.referrer)
