messege = "\n what would you like me to add to your pizza?: "
messege += "\n when youve listed everything enter quit, to stop \n"
topping = ""
while topping!= "quit":
	topping = input(messege)
	if topping != "quit":
		print("\n I will add "+topping+" to your pizza")
		

