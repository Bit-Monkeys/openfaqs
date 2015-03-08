from flask import render_template, Blueprint, session
from models import User, Tag, Question, db 

heroes = Blueprint('heroes', __name__, template_folder='templates') 

@heroes.route('/heroes')
def show_heroes(): 
	# This should send an object with user stats 
	return render_template('heroes.html', heroes=heroes) 
	
