from random import randint

class Die():
	"""a class the represents a die"""
	
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		roll = randint(1 , self.sides)
		print("the die rolls and the result is... "+str(roll)+"!")
	
		
d6 = Die()
for number in  range(0 , 10):
	d6.roll_die()
	
d10 = Die(10)
print("\nnow rolling a d10:")
for number in  range(0 , 10):
	d10.roll_die()

d20 = Die(20)
print("\nnow rolling a d20:")
for number in  range(0 , 10):
	d20.roll_die()