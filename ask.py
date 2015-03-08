from flask import render_template, request, Blueprint, session, redirect, url_for 
from models import Question, db 
from utilities import login_required

import datetime 

ask = Blueprint('ask', __name__, template_folder='templates') 

@ask.route('/ask', methods=['GET', 'POST'])  
#@login_required
def ask_question(): 
	if request.method == 'POST': 
		new_question = Question(session['UserID'],
			request.form['QuestionTitle'],
			request.form['Question'], 
			datetime.datetime.now(), 
			datetime.datetime.now())

		db.session.add(new_question)
		db.session.commit() 

		question_id = get_question_id(new_question, db)

		return redirect(url_for('questions.show_question', question_id=question_id))

	elif request.method == 'GET': 
		return render_template('ask.html')


# Helper Functions 

def get_question_id(record, db): 
	db.session.refresh(record)
	return record.ID
