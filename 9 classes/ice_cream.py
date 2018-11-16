class Restaurant():
	""" an exmple of a class representing a restaurant"""

	def __init__(self, name, cuisine):
		"""instates a restarunt with parameters for name and cuisine type"""
		self.name = name
		self.cuisine_type = cuisine
		self.number_served = 0 
		
	def describe_restaurant(self):
		""" describes the restaurant"""
		print(self.name.title()+" is a restaurant specilaizing in "+self.cuisine_type)
		
	def open_restaurant(self):
		""" sends a meesege shoes the restaurant is open"""
		print(self.name.title()+" is now open!")
		
	def set_number_served(self,served):
		"""updates the number of served customers"""
		if served>= self.number_served:
			self.number_served = served
		else:
			print("that cant be right")
	
	def increment_number_served(self, number):
		"""increseses the number of people served by the given number"""
		if number>=0:
			self.number_served+= number
		else:
			print("that cant be right")
		
		
class IceCreamStand(Restaurant):
	""" a class modeling an ice cream stand"""
	
	def __init__(self, name, cuisine="icecream", flavors=["choco", "vanilla", "strawberry"]):
		""" initalizing parameters for restaurant class then adding a list of ice cream flavers"""
		super().__init__(name, cuisine)
		self.flavors=flavors
		
	def show_flavors(self):
		"""displays the avilable flavors"""
		print("the avilable flavors are: "+str(self.flavors))

the_scope = IceCreamStand("the scope")
the_scope.describe_restaurant()
the_scope.show_flavors()