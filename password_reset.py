from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from passlib.hash import pbkdf2_sha256
from connections import app, db, mail
from forms import  ForgotPassForm, ResetPassForm
from functions import email_valid
from models import AdminModel, UserModel


@app.route("/reset_password", methods=["GET", "POST"])
def forgot_password():
    '''This function return forgot pass page and send email.
    
    Methods: 
    GET: it returns the forgot pass page
    Post: it send email to the user by calling the send email
    '''
    form = ForgotPassForm()

    if form.validate_on_submit():
        uemail = form.email.data.lower()
        utype = int(form.user_type.data)
        model = UserModel if utype == 1 else AdminModel
        is_valid_email = email_valid(uemail, model)
        
        if not is_valid_email:
            flash('Email Address Does not exists.', "emailNotUnique")
        else:   
            user = model.query.filter_by(email=uemail).first()
            send_email = send_reset_mail(utype, user)
            if send_email:
                flash("Passwrod Reset Link send to your email", category="addSuccess")
                return redirect(url_for('login'))
    
    return render_template("authentication/forgot_pass.html", form = form)



@app.route("/reset_password/<utype>/<token>", methods=["GET", "POST"])
def reset_password(utype,token):
    '''This function reset user password.
    
    Methods:
    -------
    GET: it returns the reset password page
    POST: it reset password

    parameters:
    ----------
    utype: the type of the user normal user or admin
    token: the token of the user
    '''

    model = AdminModel if utype == "admin" else UserModel
    data = model.verify_reset_token(token) #verify the token

    if data is None or data['user_type'] != utype:
        # the data['user_type'] != utype means if someone manually change the 
        # usertype in form. so first check with the type in the token
        flash("Invalid or expird token", category="loginError")
        return redirect(url_for("forgot_password"))

    form = ResetPassForm()
    if form.validate_on_submit():
        data['user'].password = pbkdf2_sha256.hash(form.new_password.data)
        db.session.commit()
        flash("Password Changed", category="addSuccess")
        return redirect(url_for('login'))
    return render_template("authentication/reset_pass.html", pass_form=form, token = token, utype=utype)



def send_reset_mail(utype, user):
    '''This function send reset password link'''
    token = user.get_reset_token()
    user_type = "user" if utype == 1 else "admin"
    msg = Message("Password Reset Link", 
        sender="bankingsystem@demo.com",
        recipients=[user.email]
        )
    msg.body = f'''\
Please Click the link Bellow to reset your bank account password

{url_for('reset_password', utype=user_type, token=token, _external=True)}
'''
    mail.send(msg)
    return True
