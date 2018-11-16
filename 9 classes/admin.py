""" classes for website  admin """
from user import User

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
		
	
		
class Admin(User):
	"""a class representing an admin of a website"""
	
	def __init__(self, first, last, age, country, user_name, privileges=["can add post", "can delete post", "can ban user"]):
		""" adds a privileges parameter to the number user set"""
		super().__init__(first, last, age, country, user_name)
		self.privileges = Privileges(privileges)