from wtforms import ValidationError
from connections import app, db


def min_money_amount(form, field):
    """This is custom validation for the amount field"""
    try:
        if int(field.data) < 100:
            raise ValidationError('Minimum 100 amount is required!')
    except:
        raise ValidationError('Minimum 100 amount is required!')


def max_money_amount(form, field):
    """This is custom validation for the amount field"""
    try:
        if int(field.data) > 100000:
            raise ValidationError('Max amount per transaction is 100,000')
    except:
        raise ValidationError('Max amount per transaction is 100,000 AFG')


def less_than_original_balance(form, field):
    from authentication import current_user
    """This is custom validation for the amount field"""
    try:
        if int(field.data) > current_user().balance:
            raise ValidationError('You have insufficient ballance')
    except:
        raise ValidationError('You have insufficient ballance')


def email_valid(uemail, model):
    from authentication import current_user
    '''This function check if the email exists in database or not.
    
    It is used when we reseting our password.

    parameters:
    -----------
    uemail: The email to be checked
    model: in which model it has to check
    '''
    user = model.query.filter_by(email=uemail).first()
    if not user:
        return False
    return True


@app.template_filter()
def number_format(value):
    """This function format the numbers with comma seperated.
    
    we call the template_filter directives here to make it availble in global
    filter in ning2 template.

    parameter:
    ----------
    value: integer, str -- the number we want to format

    Return:
    The formated value converted to integer 
    """
    return format(int(value), ',d')


# In here we pass the is_authenticated and is_admin function gloabaly
@app.context_processor
def inject_isauthenticated_and_isadmin_issupper():
    from authentication import is_authenticated, is_admin, current_user, is_supper
    return dict(is_authenticated=is_authenticated, is_admin=is_admin,
                current_user = current_user, is_supper = is_supper   
            )   