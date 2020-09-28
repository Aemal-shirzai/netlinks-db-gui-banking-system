import os
import sys
import psycopg2
from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = os.urandom(16)

app.config["SQLALCHEMY_DATABASE_URI"] ="postgresql://ubuntu:ubuntu@123@localhost/bank"
db = SQLAlchemy(app)
