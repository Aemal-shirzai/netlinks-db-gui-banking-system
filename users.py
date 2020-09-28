from flask import Flask, render_template, redirect, url_for, request, flash
from connections import app, db
from authentication import is_authenticated, is_admin, current_user
from forms import UserUpdateForm, changePasswordForm, DepositMoneyForm, WithdrawMoneyForm
from admin import email_is_unique, change_password, verify_password
from models import UserModel
from generate_recipt import Recipt


@app.route("/")
def index():
    """This function returns index page if user is a normal user."""
    # redirct if user is already authenticated
    if not is_authenticated() or is_admin():
        return redirect(url_for('login'))
    return render_template("index.html")


@app.route('/edit-profile', methods=["GET", "POST"])
def profile():
    """This function edit normal user profile."""
    # redirct if user is already authenticated
    if not is_authenticated() or is_admin():
        return redirect(url_for('login'))
    
    form = UserUpdateForm()
    pass_form = changePasswordForm()
    user = current_user()

    if request.method == "GET":
        form.name.data = user.name
        form.address.data = user.address
        form.email.data = user.email
        return render_template("edit_profile.html", form = form, \
            pass_form = pass_form)
    else:
        if form.validate():
            if not email_is_unique(UserModel, form.email.data, 'update'):
                flash("email already taken", category="emailNotUnique")
                return render_template("edit_profile.html", form=form,
                        pass_form=pass_form
                    )
            if  verify_password(form.password_verify.data):
                user.name = form.name.data
                user.address = form.address.data
                user.email = form.email.data.lower()
                db.session.commit()
                flash("User Updated", category="addSuccess")
                return redirect(url_for('profile'))
            else:
                flash("Invalid Password", category="passwordIncorrect")
                return render_template("edit_profile.html", 
                        form=form, pass_form=pass_form
                    )
        else:
            return render_template("edit_profile.html", form = form, \
            pass_form = pass_form)


@app.route('/withdraw_money', methods=["GET", "POST"])
def withdraw_money():
    """This function withdraw user money if the user is normal user."""
    # redirct if user is already authenticated
    if not is_authenticated() or is_admin():
        return redirect(url_for('login'))
    
    form = WithdrawMoneyForm()
    if request.method == "GET":
        return render_template("withdraw.html", form = form)
    else:       
        if form.validate():
            current_user().balance -= int(form.amount.data)
            db.session.commit()
            flash("Seccessfully Withdrawed", category="addSuccess")
            if form.reciept.data:
                Recipt.withdraw_reciept(current_user().balance, form.amount.data)
            return redirect(url_for('withdraw_money'))
        else:
            return render_template("withdraw.html", form = form)


@app.route("/deposit_money", methods=["GET", "POST"])
def deposit_money():
    """This function deposit money if the user is normal user."""
    # redirct if user is already authenticated
    if not is_authenticated() or is_admin():
        return redirect(url_for('login'))
    
    form = DepositMoneyForm()
    if request.method == "GET":
        return render_template("deposit.html", form = form)
    else:       
        if form.validate():
            current_user().balance += int(form.amount.data)
            db.session.commit()
            flash("Seccessfully Deposited", category="addSuccess")
            if form.reciept.data:
                Recipt.deposit_reciept(current_user().balance, form.amount.data)
            return redirect(url_for('deposit_money'))
        else:
            return render_template("deposit.html", form = form)


@app.route("/check_balance")
def check_balance():
    """This function call the generate reciept function for current balance."""
    # redirct if user is already authenticated
    if not is_authenticated() or is_admin():
        return redirect(url_for('login'))
    
    Recipt.balance_reciept()
    return redirect(request.referrer)


