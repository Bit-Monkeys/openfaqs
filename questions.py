from flask import render_template, request, Blueprint, session
from models import User, Tag, Question, db 
import datetime 


questions = Blueprint('questions', __name__, template_folder='templates') 

@questions.route('/questions')  
def show_all_questions(): 
	questions = Question.query.order_by(Question.Created.desc()).all() 
	questionList = [] 

	for question in questions: 
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
		questionList.append(question)  

	return render_template('questions.html', questions=questionList)

@questions.route('/questions/<question_id>')
def show_question(question_id): 
	question = Question.query.filter_by(ID=question_id).first() 

	return render_template('questions.html', questions=question) 
	