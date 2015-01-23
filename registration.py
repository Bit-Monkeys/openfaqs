from flask import Blueprint, request, render_template
from models import db, User 
from sessions import login 
from utilities import hash_password

import datetime 

registration = Blueprint('registration', __name__, template_folder='templates')


@registration.route('/register', methods=['GET', 'POST']) 
def register(): 
	if request.method == 'POST': 
		password = hash_password(request.form['password']) 

		new_user = User(request.form['firstname'],
			request.form['firstname'], 
			request.form['username'], 
			request.form['email'], 
			password, 
			datetime.datetime.now(), 
			datetime.datetime.now(), 
			True)

		db.session.add(new_user)
		db.session.commit() 

		login()

		return render_template('dashboard.html') 	

	else: 
		return render_template('register.html') 