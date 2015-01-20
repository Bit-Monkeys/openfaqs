import yaml 

from flask import Flask, render_template, Blueprint
from models import db 

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

# Register Blueprints 
app.register_blueprint(registration)
app.register_blueprint(sessions) 

with app.app_context(): 
	db.create_all()
	db.session.commit() 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index(): 
	return render_template('bootshell.htm')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True) 