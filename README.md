## Netlinks - Banking System
This is a simple web base GUI banking system , built with python flask and postgresql.<br>
In this system we have 3 types of users:
1. **Super Admin**: ability to perform any kind of tasks in the system. (Only have one in the system)
  - Edit Profile 
  - Add Users
  - Delete Users
  - Add admins
  - Delete Admins
2. **Normal Admin**: can perform same tasks as super admin except adding another admin and deleting them.
  - Edit Profile
  - Add Users
  - Delete Users
3. **Normal User**: which only perform tasks related to their accounts. They are added by admins.
  - Edit profile basic information (can not delete accoun)
  - Deposit Money
  - Withdraw Money
  - Check Balance

**Users can also reset their password**
 
## Prerequisites Modules To Install
1. Python3: [(Linux)](https://docs.python-guide.org/starting/install3/linux/)  [(windows)](https://docs.python-guide.org/starting/install3/win/)4
2. PostgreSQL: For database [(Linux)](https://tecadmin.net/install-postgresql-server-on-ubuntu/) [(Wiindows)](https://www.guru99.com/download-install-postgresql.html)
3. Flask: [Install](https://flask.palletsprojects.com/en/1.1.x/installation/)
4. Falsk-wtf: Used to handle forms in flask. [Install](https://flask-wtf.readthedocs.io/en/stable/install.html)
5. email_validator: To validate email fields. It is part of flask-wtf. 

     ```
     pip3 install email_validator
     ```
     
6. SQLAlchemy: SQLAlchemy is a popular SQL toolkit and Object Relational Mapper. 

    ````
    pip3 install Flask-SQLAlchemy
    ````
    
7. Flask-Migrate: Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.

    ```
    pip3 install Flask-Migrate
    ```

8. Flask-Script: The Flask-Script extension provides support for writing external scripts in Flask.

    ```
    pip3 install Flask-Script
    ```

9. pylint-flask: pylint-flask is a Pylint plugin to aid Pylint in recognizing and understanding errors caused when using Flask.

    ```
    pip3 install pylint-flask
    ```

10. passlib: Passlib is a password hashing library for Python 2 & 3, which provides cross-platform implementations. 

    ```
    pip3 install passlib
    ```

11. flask-mail: The Flask-Mail extension provides a simple interface to set up SMTP with your Flask application and to send messages from your views and scripts. 

    ```
    pip3 install Flask-Mail
    ```
 
 ## Project Structure
 
 **Python Files**<br>
   1. connections.py: This file create flask app, generate secrete key for our app and connect to postgresql database.
   2. main.py: This file is the entry pase of our app it runs the app.
   3. migrations.py: This file contains the datbase migrations. our table structure.
   4. seed.py: This file contains the data to be seeded to database for first time.
   5. models.py: This file contains models of our tables. Each class represet a table in the database.
   6. password_reset.py: this file contains functions to reset user password
   7. forms.py: This file has our all forms classes. using the wtforms.
   8. authentication.py: This file has login, logout and also functions to keep user track.
   9. functions.py: This file include some cusom validation functions and functions used globaly in the templates.
   1. users.py: This file contain all functions to be used when working as normal user.
   11. admin.py: This file contain all functions to be used when working as admin user. and some functions can be accessed from user.py file too.
   12. generate_reciept.py: This file generate user reciepts for chekcing, withdrawing and depositing money.

**Template Files** <br>
   1. Admin Dirctory: Contain all admin related templates.
   2. Authentiation Directory: Contain all templates realted to authentication and passwrod reset
   3. Layouts Directory: Contain main template for our project.
   4. Other files are related to normal user
 
 **Assets Files**<br>
   1. static folder: contains all the assests files
      - Css: All css files
      - Js:  All Javascript and jquery files
     

## How To Run
1. You should have python and postgresql installed in your system.
2. Download the project.
3. Go to connections file and edit your postgresql database URI and database name.
4. You should set the email configurations in connections file aswell. if you use smtp.gmail.com then you should have a app password for your gmail account. go and create one before proceeding. and alsow edit the configurations
5. Run Migrations: Go to the project dirctory and run the following commands:
   
   ```
   python3 migrations.py db init
   python3 migrations.py db migrate
   python3 migrations.py db upgrade
   ```
   
6. Seed data: Add one super admin by running the seed file:

   ```
   python3 seed.py
   ```

7. export App:
   
   
   ```
   export FLASK_APP=man.py
   ```

7. Run File:
   
   ```
   flask run
   ```
