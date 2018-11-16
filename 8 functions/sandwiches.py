def make_sandwich(*ingridients):
	print("\nmaking a sandwich useing the following ingridents")
	for ingridient in ingridients:
		print("- "+ingridient)
		
make_sandwich("tomato", "cheese", "pepers")
make_sandwich("ham", "lettece")
make_sandwich("avocado", "egg", "lettece" , "halapinio")
		