from flask import Blueprint, request 
from models import User, db 
from functools import wraps, update_wrapper

import hashlib

utilities = Blueprint('utilities', __name__, template_folder='templates')

def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        try:
            session['Username']
        except:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorator

def hash_password(password):
    m = hashlib.sha256()
    m.update(password)
    m.update("6gwxK6VMR3MZV7AnD6ZgsRtKvQHtWo")
    return m.hexdigest() 

# Ajaxy Things
@utilities.route('/ajax/checkusername', methods=['GET'])
def ajax_check_username(): 
	if 'username' in request.args: 
		check = check_username(request.args.get('username'))
		return str(check) 
	else: 
		return 'error'

@utilities.route('/ajax/checkemail', methods=['GET'])
def ajax_check_email(): 
	if 'email' in request.args: 
		check = check_email(request.args.get('email'))
		return str(check) 
	else: 
		return 'error'

# Helper Functions 
def check_username(username):
    check = User.query.filter_by(UserName=username).first()
    if check:
        return False
    else:
        return True

def check_email(email): 
	check = User.query.filter_by(Email=email).first() 
	if check: 
		return False 
	else: 
		return True 
