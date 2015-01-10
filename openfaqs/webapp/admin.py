from django.contrib import admin
from webapp.models import *
# Register your models here.
class QuestionInline(admin.TabularInline):
	model = Question
admin.site.register(Question)
	
