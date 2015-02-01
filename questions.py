from flask import render_template, request, Blueprint, session
from models import User, Tag, Question, db 
import datetime 


questions = Blueprint('questions', __name__, template_folder='templates') 

@questions.route('/questions/<question_id>')
def show_question(question_id): 
	question = Question.query.filter_by(ID=question_id).first() 
	user = User.query.filter_by(ID = question.UserID).first() 

	question = { 
			'UserName': user.UserName,
			'Title': question.Title, 
			'Question' : question.QuestionText,
			'Date' : question.Created, 
			'Tags' : question.tags, 
			'Votes' : "10", 
			'Answers' : "10", 
			'Views' : "100" 
		}

	return render_template('questions.html', question=question) 
	