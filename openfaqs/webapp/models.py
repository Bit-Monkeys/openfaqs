from django.db import models

class User(models.Model):
	UserName = models.CharField(max_length=50)
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Password = models.CharField(max_length=1000)
	Created = models.DateTimeField()
	Modified = models.DateTimeField()

class UserSettings(models.Model):
	UserID = models.ForeignKey(User)
	isAdmin = models.BooleanField(default=False)

class Tag(models.Model):
	Tag = models.CharField(max_length=50)	
	
class Question(models.Model):
	UserID= models.ForeignKey(User)
	Title = models.CharField(max_length=200)
	QuestionText = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()
	
class QuestionTag(models.Model):
	QuestionID=models.ForeignKey(Question)
	TagID = models.ForeignKey(Tag)

class QuestionComment(models.Model):
	QuestionID = models.ForeignKey(Question)
	UserID = models.ForeignKey(User)
	Comment = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()

class QuestionVote(models.Model):
	UserID = models.ForeignKey(User)
	QuestionID = models.ForeignKey(Question)
	Value = models.IntegerField()

class QuestionAttachment(models.Model):
	QuestionID = models.ForeignKey(Question)
	FilePath = models.CharField(max_length=100)

class Answer(models.Model):
	QuestionID = models.ForeignKey(Question)
	UserID = models.ForeignKey(User)
	Answer = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()
	
class AnswerAttachment(models.Model):
	AnswerID = models.ForeignKey(Answer)
	FilePath = models.CharField(max_length=100)

class AnswerVote(models.Model):
	UserID = models.ForeignKey(User)
	AnswerId = models.ForeignKey(Answer)
	Value = models.IntegerField()

class Comment(models.Model):
	AnswerID = models.ForeignKey(Answer)
	UserID = models.ForeignKey(User)
	Comment = models.TextField()
	CreatedTime = models.DateTimeField()
	ModifiedTime = models.DateTimeField()

class Badge(models.Model):
	Description = models.CharField(max_length=100)
	FilePath = models.CharField(max_length=100)

class UserBadge(models.Model):
	UserID = models.ForeignKey(User)
	BadgeID = models.ForeignKey(Badge)

