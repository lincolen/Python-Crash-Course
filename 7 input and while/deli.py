sandwich_orders=["pastrami","scrambled egg","guwacamoli","pizzatost","pastrami","pastrami",]
if "pastrami" in sandwich_orders:
	print("Im very sorry but weave run out of pastrami, so ill cancel your order")
	while "pastrami" in sandwich_orders:
		sandwich_orders.remove("pastrami")
finished_sandwiches=[]
while sandwich_orders:
	finished_sandwich=sandwich_orders.pop()
	print("youre "+finished_sandwich+" sandwich is ready")
	finished_sandwiches.append(finished_sandwich)
print(str(finished_sandwiches)+"\n were completed")