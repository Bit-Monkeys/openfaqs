from flask import render_template, request 
from models import Question, db 
import datetime 

ask = Blueprint('ask', __name__, template_folder='templates') 

@app.route('/ask')
def ask(): 
	return render_template('ask.html')

@app.route('/ask/submit' methods=['GET', 'POST'])  
def ask_submit(): 
	if request.method == 'POST': 
		new_question = Question(session['user_id'],
			request.form['title'],
			request.form['question_text'], 
			datetime.datetime.now(), 
			datetime.datetime.now())

		db.session.add(new_question)
		db.session.commit() 

		question_id = get_question_id(new_question, db)

		return render_template('questions.html', question=question_id)

# Helper Functions 

def get_question_id(record, db): 
	db.session.refresh(record)
	return record.id 