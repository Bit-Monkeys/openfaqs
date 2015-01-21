from flask import Blueprint, request 
from models import User, db 
import md5 

utilities = Blueprint('utilities', __name__, template_folder='templates')

def hash_password(password): 
	m = md5.new() 
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