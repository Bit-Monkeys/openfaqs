from flask import Blueprint, request, session, redirect 
from models import User 
from utilities import hash_password

sessions = Blueprint('sessions', __name__, template_folder='templates') 

def check_login():
	try: 
		if session['username']: 
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
			session['user_id'] = find_user.ID 
			session['username'] = find_user.UserName 
			session['email'] = find_user.Email 
			
			return redirect('/dashboard') 

		else: 

			return render_template('error.html', error="Invalid credentials, please try again.") 

	else: 
		render_template('error.html') 

@sessions.route('/logout', methods=['GET'])
def logout(): 
	session.pop('user_id', None) 
	session.pop('username', None) 
	session.pop('email', None)

	return render_template('index.html', message="You have been logged out.") 