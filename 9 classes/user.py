"""class for a websites user"""

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