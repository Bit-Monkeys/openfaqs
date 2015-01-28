from flask import render_template, request, Blueprint, session
from models import Question, db 
import datetime 

questions = Blueprint('questions', __name__, template_folder='templates') 

@questions.route('/questions')  
def show_question(): 
	questions = Question.query.all() 

	return render_template('questions.html', questions=questions)


