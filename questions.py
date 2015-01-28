from flask import render_template, request, Blueprint, session
from models import Question, db 
import datetime 

questions = Blueprint('questions', __name__, template_folder='templates') 

@questions.route('/questions')  
def show_all_questions(): 
	questions = Question.query.order_by(Question.Created.desc()).all() 

	return render_template('questions.html', questions=questions)

@questions.route('/questions/<question_id>')
def show_question(question_id): 
	question = Question.query.filter_by(ID=question_id).first() 

	return render_template('questions.html', questions=question) 
	