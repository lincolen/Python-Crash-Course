class User():
	""" a class exampling a user profile in a website"""
	
	def __init__(self, first, last, age, country, user_name):
		""" builds the user profile with name age country and user name attributes"""
		self.first_name = first
		self.last_name = last
		self.age = age
		self.country = country
		self.user_name = user_name
		
	def user_details(self):
		"""dsiplays a summery of the users details"""
		print("\n"+"username: "+self.user_name+", real name: "+self.first_name.title()+" "+self.last_name.title()
			+"\nage: "+str(self.age)+", country: "+self.country.title())
			
	def hello(self):
		"""sends a hello messege to the user"""
		print("\n"+"hello "+self.user_name+"!")
		
		
korra = User("korra", "avatar", 20, "south water tribe", "probender5564")
tsuku = User("tsuku", "flame", 84, "fire nation", "Dfirelord")
aang = User("aang", "the last", 15, "northern air temple", "little apa")

korra.user_details()
tsuku.user_details()
aang.user_details()

korra.hello()
tsuku.hello()
aang.hello()