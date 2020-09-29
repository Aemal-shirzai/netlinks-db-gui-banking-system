import os
import sys
import psycopg2
from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = os.urandom(16)

app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://ubuntu:ubuntu@123@localhost/bank"
db = SQLAlchemy(app)

# mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'aemalshirzai2016@gmail.com'
app.config['MAIL_PASSWORD'] = 'fhmg vwhg iubw ofaa'

mail = Mail(app)


