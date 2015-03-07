from flask import Blueprint, request, session, redirect, render_template
from models import User 
from utilities import hash_password

sessions = Blueprint('sessions', __name__, template_folder='templates') 

def check_login():
	try: 
		if session['UserName']: 
			return True 
	except: 
		return False 

@sessions.route('/login', methods=['POST', 'GET']) 
def login(): 
	if request.method == 'POST': 

		password_hashed = hash_password(request.form['password']) 
		find_user = User.query.filter_by(UserName=request.form['username'],
			Password=password_hashed).first() 

		if find_user: 
			session['UserID'] = find_user.ID 
			session['UserName'] = find_user.UserName 
			session['Email'] = find_user.Email 
			
			return redirect('/') 

		else: 

			return render_template('error.html', error="Invalid credentials, please try again.") 

	else: 
		return render_template('loginmodal.html') 

@sessions.route('/logout', methods=['GET'])
def logout(): 
	session.pop('UserID', None) 
	session.pop('UserName', None) 
	session.pop('Email', None)

	return render_template('index.html', message="You have been logged out.") 