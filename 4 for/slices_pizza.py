pizzas=["margarita","corn-halapinio","tomato-olive"]
friend_pizzas=pizzas[:]
pizzas.append("anchobi")
friend_pizzas.append("pineaple")
print("my favorite pizzas are:")
for pizza in pizzas:
	print("\t"+pizza)
print("my friends favorite pizzas are:"	)
for pizza in friend_pizzas:
	print("\t"+pizza)	
print(" damn now I want to eat pizza")