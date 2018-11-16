class User():
	""" a class exampling a user profile in a website"""
	
	def __init__(self, first, last, age, country, user_name):
		""" builds the user profile with name age country and user name attributes"""
		self.first_name = first
		self.last_name = last
		self.age = age
		self.country = country
		self.user_name = user_name
		self.login_attempts = 0
		
	def user_details(self):
		"""dsiplays a summery of the users details"""
		print("\n"+"username: "+self.user_name+", real name: "+self.first_name.title()+" "+self.last_name.title()
			+"\nage: "+str(self.age)+", country: "+self.country.title())
			
	def hello(self):
		"""sends a hello messege to the user"""
		print("\n"+"hello "+self.user_name+"!")
	
	def increment_login_attempts(self):
		""" increses the number of login attempts by the user by one"""
		self.login_attempts+=1
		
	def reset_login_attempts(self):
		""" resets the number of login attempts made by the user (ergo succsesful login) """
		self.login_attempts = 0
		
		
		
bang = User("bang", "shishigami", 43, "ikaruga", "litchiLV")
bang.increment_login_attempts()
bang.increment_login_attempts()
bang.increment_login_attempts()
bang.increment_login_attempts()
bang.increment_login_attempts()
bang.increment_login_attempts()
print("number of times user "+bang.user_name+" has attempted to login is "+str(bang.login_attempts))
bang.reset_login_attempts()
print("number of times user "+bang.user_name+" has attempted to login is "+str(bang.login_attempts))