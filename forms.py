from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, ValidationError, BooleanField
from wtforms.fields.html5 import IntegerField
import email_validator
from wtforms.validators import InputRequired, Regexp, Email, Length, EqualTo
from models import AdminModel
from functions import min_money_amount, max_money_amount, less_than_original_balance

class LoginForm(FlaskForm):
    """This Class contains inputs and their validation.
    
    This class is blueprint for login forms. it has email input field and
    passwrod input field alongside thier validations.

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    email = StringField(
        label="Email Address",
        id="email",
        render_kw={
            'placeholder':'Email Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Email Field"), 
            Email("Invalid Email Address"),
            Length(max=30, message="Too Long Email supplied")
        ]
    )
    password = PasswordField(
        label="Passwrod",
        id="password",
        render_kw={'placeholder':'Password', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Password Field"), 
            Length(max=100, message="Too Long Password supplied"),
        ],
    )
    user_type = SelectField(
        choices=[(1,"User"),(2,"Admin")],
        validators=[InputRequired("Choose your type")],
        render_kw={"class":"form-control"}
    )


class AdminRegisterForm(FlaskForm):
    """This Class contains inputs and their validation.
    
    This class is blueprint for admin registration forms. It has name, email,
    password and confirm password field

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    name = StringField(
        label="Name",
        id="name",
        render_kw={
            'placeholder':'Admin Name', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the name Field"), 
            Regexp(regex="^[a-zA-z]+", message="Name is invalid"),
            Length(max=30, message="Too Long Name supplied")
        ]
    )
    email = StringField(
        label="Email Address",
        id="email",
        render_kw={
            'placeholder':'Email Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Email Field"), 
            Email("Invalid Email Address"),
            Length(max=40, message="Too Long Email supplied")
        ]
    )
    password = PasswordField(
        label="Passwrod",
        id="password",
        render_kw={'placeholder':'Password', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Password Field"), 
            Length(min=6, max=40),
            EqualTo("confirm", message="Password must match!!")
        ],
    )
    confirm = PasswordField(
        label="Passwrod confirm",
        id="confirm",
        render_kw={'placeholder':'Password', 'class':'form-control'},
    )


class AdminUpdateForm(FlaskForm):
    """This Class contains inputs and their validation.
    
    This class is blueprint for amdin update forms. It Has name and email field

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    name = StringField(
        label="Name",
        id="name",
        render_kw={
            'placeholder':'Admin Name', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the name Field"), 
            Regexp(regex="^[a-zA-z]+", message="Name is invalid"),
            Length(max=30, message="Too Long Name supplied")
        ]
    )
    email = StringField(
        label="Email Address",
        id="email",
        render_kw={
            'placeholder':'Email Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Email Field"), 
            Email("Invalid Email Address"),
            Length(max=40, message="Too Long Email supplied")
        ]
    )
    password_verify = PasswordField(
        label="Password for conrimation",
        id="password_verify",
        render_kw={'placeholder':'confirmation pass', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill  Password Field"), 
            Length(min=6, max=40),
        ],
    )


class UserRegisterForm(FlaskForm):
    """This Class contains inputs and their validation.
    
    This class is blueprint for User Registrations forms. It has name, address,
    email, password and confirm password fields.

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    name = StringField(
        label="Name",
        id="name",
        render_kw={
            'placeholder':'User Name', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the name Field"), 
            Regexp(regex="^[a-zA-z]+", message="invalid name"),
            Length(max=30, message="Too Long Name supplied")
        ]
    )
    address = StringField(
        label="Address",
        id="address",
        render_kw={
            'placeholder':'Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Address Field"), 
            Length(max=50, message="Too Long Address supplied")
        ]
    )
    email = StringField(
        label="Email Address",
        id="email",
        render_kw={
            'placeholder':'Email Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Email Field"), 
            Email("Invalid Email Address"),
            Length(max=40, message="Too Long Email supplied")
        ]
    )
    password = PasswordField(
        label="Passwrod",
        id="password",
        render_kw={'placeholder':'Password', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Password Field"), 
            Length(min=6, max=40),
            EqualTo("confirm", message="Password must match!!")
        ],
    )
    confirm = PasswordField(
        label="Passwrod confirm",
        id="confirm",
        render_kw={'placeholder':'Password', 'class':'form-control'},
    )


class UserUpdateForm(FlaskForm):
    """This Class contains inputs and their validation.
    
    This class is blueprint for users update forms. It Has name and email field

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    name = StringField(
        label="Name",
        id="name",
        render_kw={
            'placeholder':'Admin Name', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the name Field"), 
            Regexp(regex="^[a-zA-z]+", message="invalid name"),
            Length(max=30, message="Too Long Name supplied")
        ]
    )
    address = StringField(
        label="Address",
        id="address",
        render_kw={
            'placeholder':'Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Address Field"), 
            Length(max=50, message="Too Long Address supplied")
        ]
    )
    email = StringField(
        label="Email Address",
        id="email",
        render_kw={
            'placeholder':'Email Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Email Field"), 
            Email("Invalid Email Address"),
            Length(max=40, message="Too Long Email supplied")
        ]
    )
    password_verify = PasswordField(
        label="Password for conrimation",
        id="password_verify",
        render_kw={'placeholder':'confirmation pass', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill  Password Field"), 
            Length(min=6, max=40),
        ],
    )


class changePasswordForm(FlaskForm):
    """This Class contains inputs and their validation .
    
    This class is blueprint for change pass forms. old pass, new pass and 
    confirm new password filds.
    It is shared by both users and admins

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    old_password = PasswordField(
        label="Old Password",
        id="old_password",
        render_kw={'placeholder':'Old Password', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Old Password Field"), 
            Length(min=6, max=40),
        ],
    )
    new_password = PasswordField(
        label="New Passwrod",
        id="new_password",
        render_kw={'placeholder':'New Password', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Password Field"), 
            Length(min=6, max=40),
            EqualTo("confirm", message="Password must match!!")
        ],
    )
    confirm = PasswordField(
        label="Passwrod confirm",
        id="confirm",
        render_kw={'placeholder':'Password', 'class':'form-control'},
    )


class DepositMoneyForm(FlaskForm):
    """This Class contains inputs and their validation .
    
    This Calss represet the depsit money forms.

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    amount = StringField(
        label="Amount",
        id="amount",
        render_kw={'placeholder':'Amount...', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Field"),
            Regexp(regex="^([\s\d]+)$", message="only digits are allowed!"),
            min_money_amount,
            max_money_amount,
        ],
    )
    reciept = BooleanField(
        label="want a reciept for transaction?",
        id="reciept"
    )


class WithdrawMoneyForm(FlaskForm):
    """This Class contains inputs and their validation .
    
    This Calss represet the withdraw money forms.

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    amount = StringField(
        label="Amount",
        id="amount",
        render_kw={'placeholder':'Amount...', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Field"),
            Regexp(regex="^([\s\d]+)$", message="only digits are allowed!"),
            min_money_amount,
            max_money_amount,
            less_than_original_balance
        ],
    )
    reciept = BooleanField(
        label="want a reciept for transaction?",
        id="reciept"
    )


class ForgotPassForm(FlaskForm):
    """This Class contains inputs and their validation.
    
    This class is blueprint for login forms. it has email input field.

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    email = StringField(
        label="Email Address",
        id="email",
        render_kw={
            'placeholder':'Email Address', 'class':'form-control',
            'autocomplete':'off'
        },
        validators=[
            InputRequired("Please Fill the Email Field"), 
            Email("Invalid Email Address"),
            Length(max=30, message="Too Long Email supplied"),
        ],
    )
    user_type = SelectField(
        choices=[(1,"User"),(2,"Admin")],
        validators=[InputRequired("Choose your type")],
        render_kw={"class":"form-control"}
    )



class ResetPassForm(FlaskForm):
    """This Class contains inputs and their validation .
    
    This class is blueprint for change pass forms. new pass and 
    confirm new password filds.
    It is shared by both users and admins

    Parameters:
    ----------
    FlaskForm: it used to inherate the FlaskForm
    """
    new_password = PasswordField(
        label="New Passwrod",
        id="new_password",
        render_kw={'placeholder':'New Password', 'class':'form-control'},
        validators=[
            InputRequired("Please Fill the Password Field"), 
            Length(min=6, max=40),
            EqualTo("confirm", message="Password must match!!")
        ],
    )
    confirm = PasswordField(
        label="Passwrod confirm",
        id="confirm",
        render_kw={'placeholder':'Password', 'class':'form-control'},
    )

