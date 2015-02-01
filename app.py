import yaml 

from flask import Flask, render_template, request, Blueprint, session
from models import User, Tag, Question, db 
import datetime 

# Configuration for the App 

config = open("config/settings.yaml", "r") 
settings = yaml.load(config) 

connection = "mysql://%s:%s@%s:3306/%s" % (
	settings['username'], settings['password'], 
	settings['hostname'], settings['database'])

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = connection 
app.secret_key = settings['secret_key']
db.init_app(app) 

# Load Blueprints 
from registration import registration 
from sessions import sessions 
from utilities import utilities 
from ask import ask 
from questions import questions

# Register Blueprints 
app.register_blueprint(registration)
app.register_blueprint(sessions) 
app.register_blueprint(utilities)
app.register_blueprint(ask) 
app.register_blueprint(questions)

with app.app_context(): 
	db.create_all()
	db.session.commit() 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')  
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

	return render_template('index.html', questions=questionList)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True) 