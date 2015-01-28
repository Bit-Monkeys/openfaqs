from flask import render_template, request, Blueprint, session, redirect 
from models import Question, db 
import datetime 

ask = Blueprint('ask', __name__, template_folder='templates') 

@ask.route('/ask', methods=['GET', 'POST'])  
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

		return redirect('/questions')

	elif request.method == 'GET': 
		return render_template('ask.html')


# Helper Functions 

def get_question_id(record, db): 
	db.session.refresh(record)
	return record.ID