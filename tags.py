from flask import render_template, request, Blueprint, session
from models import User, Tag, Question, db 
import datetime 

tags = Blueprint('tags', __name__, template_folder='templates') 

@tags.route('/tags')
def show_tags(): 
	# Show all tags statistics 
	return render_template('tags.html', tags=tags) 
	
@tags.route('/tags/<tag>')
def show_tag(tag): 
	# Show all questions that have a specific tag 
	return render_tempalte('tags.html', tag)
