class Restaurant():
	""" an exmple of a class representing a restaurant"""

	def __init__(self, name, cuisine):
		"""instates a restarunt with parameters for name and cuisine type"""
		self.name = name
		self.cuisine_type = cuisine
		
	def describe_restaurant(self):
		""" describes the restaurant"""
		print(self.name.title()+" is a restaurant specilaizing in "+self.cuisine_type)
		
	def open_restaurant(self):
		""" sends a meesege shoes the restaurant is open"""
		print(self.name.title()+" is now open!")
		

bavarn = Restaurant("bavaran", "Bavarian food")
print(bavarn.name.title())
print(bavarn.cuisine_type)
bavarn.describe_restaurant()
bavarn.open_restaurant()

gormwolf = Restaurant("gormwolf", "meats")
gormwolf.describe_restaurant()

maharuby = Restaurant("maharuby", "Indien food")
maharuby.describe_restaurant()