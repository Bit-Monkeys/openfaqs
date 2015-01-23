from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

# Assocaition Tables 
question_tag = db.Table(
	'QuestionTag', 
	db.Column(
		'QuestionID', 
		db.Integer, 
		db.ForeignKey('question.ID', ondelete="CASCADE")),
	db.Column(
		'TagID', 
		db.Integer, 
		db.ForeignKey('tag.ID', ondelete="CASCADE")))

user_badge = db.Table(
	'UserBadge', 
	db.Column(
		'UserID', 
		db.Integer,
		db.ForeignKey('user.ID', ondelete="CASCADE")),
	db.Column(
		'BadgeID', 
		db.Integer, 
		db.ForeignKey('badge.ID', ondelete="CASCADE")))


class User(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	UserName = db.Column(db.String(50), unique=True)
	FirstName = db.Column(db.String(50))
	LastName = db.Column(db.String(50)) 
	Email = db.Column(db.String(100), unique=True)
	Password = db.Column(db.String(200))
	Created = db.Column(db.DateTime) 
	Modified = db.Column(db.DateTime) 

	settings = db.relationship("UserSettings", backref="User") 
	questions = db.relationship("Question", backref="User") 
	questioncomments = db.relationship("QuestionComment", backref="User")
	questionvotes = db.relationship("QuestionVote", backref="User") 
	answers = db.relationship("Answer", backref="User")
	answercomments = db.relationship("AnswerComment", backref="User")
	answervotes = db.relationship("AnswerVote", backref="User")

	def __init__(self, FirstName, LastName, UserName, Email, Password, Created, Modified):
		self.FirstName = FirstName 
		self.LastName = LastName 
		self.UserName = UserName 
		self.Email = Email 
		self.Password = Password 
		self.Created = Created 
		self.Modified = Modified 

class UserSettings(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE"))
	isAdmin = db.Column(db.Boolean, default=True) 

	def __init__(self, UserID, isAdmin):
		self.UserID = UserID 
		self.isAdmin = isAdmin 

class Tag(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	Tag = db.Column(db.String(100))

	def __init__(self, Tag): 
		self.Tag = Tag 

class Question(db.Model): 
	ID = db.Column(db.Integer, primary_key=True)
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE")) 
	Title = db.Column(db.String(500)) 
	QuestionText = db.Column(db.Text)
	Created = db.Column(db.DateTime) 
	Modified = db.Column(db.DateTime) 

	comments = db.relationship("QuestionComment", backref="Question") 
	votes = db.relationship("QuestionVote", backref="Question")
	attachments = db.relationship("QuestionAttachment", backref="Question")
	answers = db.relationship("Answer", backref="Question") 

	def __init__(self, UserID, Title, QuestionText, Created, Modified): 
		self.UserID = UserID 
		self.Title = Title 
		self.QuestionText = QuestionText 
		self.Created = Created 
		self.Created = Created 

class QuestionComment(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	QuestionID = db.Column(db.Integer, db.ForeignKey('question.ID', ondelete="CASCADE"))
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE"))
	Comment = db.Column(db.Text)
	Created = db.Column(db.DateTime) 
	Modified = db.Column(db.DateTime) 

	def __init__(self, QuestionID, UserID, Comment, Created, Modified): 
		self.QuestionID = QuestionID 
		self.UserID = UserID 
		self.Comment = Comment 
		self.Created = Created 
		self.Modified = Modified 

class QuestionVote(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	QuestionID = db.Column(db.Integer, db.ForeignKey('question.ID', ondelete="CASCADE"))
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE"))
	Value = db.Column(db.Integer)

	def __init__ (self, QuestionID, UserID, Value): 
		self.QuestionID = QuestionID 
		self.UserID = UserID 
		self.Value = Value 

class QuestionAttachment(db.Model): 
	ID = db.Column(db.Integer, primary_key=True)
	QuestionID = db.Column(db.Integer, db.ForeignKey('question.ID', ondelete="CASCADE"))
	FilePath = db.Column(db.String(100)) 

	def __init__ (self, QuestionID, FilePath): 
		self.QuestionID = QuestionID 
		self.FilePath = Filepath 

class Answer(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	QuestionID = db.Column(db.Integer, db.ForeignKey('question.ID', ondelete="CASCADE"))
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE"))
	Answer = db.Column(db.Text) 
	Created = db.Column(db.DateTime) 
	Modified = db.Column(db.DateTime)

	votes = db.relationship("AnswerVote", backref="Answer")
	attachments = db.relationship("AnswerAttachment", backref="Answer") 
	comments = db.relationship("AnswerComment", backref="Answer") 

	def __init__(self, QuestionID, UserID, Answer, Created, Modified): 
		self.QuestionID = QuestionID 
		self.UserID = UserID 
		self.Answer = Answer 
		self.Created = Created 
		self.Modified = Modified 

class AnswerVote(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	AnswerID = db.Column(db.Integer, db.ForeignKey('answer.ID', ondelete="CASCADE"))
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE"))
	Value = db.Column(db.Integer)

	def __init__ (self, AnswerID, UserID, Value): 
		self.AnswerID = AnswerID 
		self.UserID = UserID 
		self.Value = Value 

class AnswerAttachment(db.Model): 
	ID = db.Column(db.Integer, primary_key=True)
	AnswerID = db.Column(db.Integer, db.ForeignKey('answer.ID', ondelete="CASCADE"))
	FilePath = db.Column(db.String(100)) 

	def __init__ (self, AnswerID, FilePath): 
		self.AnswerID = AnswerID 
		self.FilePath = Filepath 

class AnswerComment(db.Model): 
	ID = db.Column(db.Integer, primary_key=True) 
	AnswerID = db.Column(db.Integer, db.ForeignKey('answer.ID', ondelete="CASCADE"))
	UserID = db.Column(db.Integer, db.ForeignKey('user.ID', ondelete="CASCADE"))
	Comment = db.Column(db.Text)
	Created = db.Column(db.DateTime) 
	Modified = db.Column(db.DateTime) 

	def __init__(self, AnswerID, UserID, Comment, Created, Modified): 
		self.AnswerID = AnswerID 
		self.UserID = UserID 
		self.Comment = Comment 
		self.Created = Created 
		self.Modified = Modified 

class Badge(db.Model): 
	ID = db.Column(db.Integer, primary_key=True)
	Description = db.Column(db.String(200))
	FilePath = db.Column(db.String(200)) 

	def __init__(self, Description, Filepath): 
		self.Description = Description
		self.Filepath = Filepath