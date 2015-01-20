import md5 

def hash_password(password): 
	m = md5.new() 
	m.update(password) 
	m.update("6gwxK6VMR3MZV7AnD6ZgsRtKvQHtWo")
	return m.hexdigest() 
