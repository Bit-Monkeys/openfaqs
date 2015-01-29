from flask import render_template, request, Blueprint, session
from models import User, Tag, Question, db 
import datetime 
import json 

questions = Blueprint('questions', __name__, template_folder='templates') 

@questions.route('/questions')  
def show_all_questions(): 
	questions = Question.query.order_by(Question.Created.desc()).all() 
	questionList = [] 

	for question in questions: 
		user = User.query.filter_by(ID = question.UserID).first() 
		date = json.dumps(question.Created.isoformat())

		tags = {'tag' : row.Tag for row in question.tags }

		question = { 
			'UserName': user.UserName,
			'Title': question.Title, 
			'Question' : question.QuestionText,
			'Date' : date, 
			'Tags' : tags, 
			'Votes' : "10", 
			'Answers' : "10", 
			'Views' : "100" 
		}
		questionList.append(question)  

	json_questions = json.dumps(questionList)

	return render_template('questions.html', questions=json_questions)

@questions.route('/questions/<question_id>')
def show_question(question_id): 
	question = Question.query.filter_by(ID=question_id).first() 

	return render_template('questions.html', questions=question) 
	