import os
import sys
import psycopg2
from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail


app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = os.urandom(16)

app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://username:password@host/databasename"
db = SQLAlchemy(app)
app.config['SESSION_COOKIE_SECURE'] = True
# mail configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gmail username'
app.config['MAIL_PASSWORD'] = 'gmail application password'


mail = Mail(app)


