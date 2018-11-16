class Privileges():
	"""a class that handeles the privileges of an admin user"""
	
	def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
		self.privileges = privileges
		
	def show_privileges(self):
		"""show the privileges avilable"""
		print("Admin  can use the following privileges: "+str(self.privileges))

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
		
class Admin(User):
	"""a class representing an admin of a website"""
	
	def __init__(self, first, last, age, country, user_name, privileges=["can add post", "can delete post", "can ban user"]):
		""" adds a privileges parameter to the number user set"""
		super().__init__(first, last, age, country, user_name)
		self.privileges = Privileges(privileges)
		

hiro_privileges = ["make a user tea", "give user criptic life advice", "not ever die"]
admin_hiro = Admin("hiro", "uncle", 64, "firenation",  "jasmintea", hiro_privileges)
admin_hiro.privileges.show_privileges()
