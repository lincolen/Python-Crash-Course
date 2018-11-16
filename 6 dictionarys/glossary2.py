glossary={
	'pyhton' : "A programing langauge with simple syntex",
	'list' : "pythons version of an array. used to keep a series of values",
	'slice' : "A partial potrtion of a list",
	'tuple' : "An unwrittble list",
	'dictionary' : "a series of key-values sets",
	}
glossary["set"]="a function that creats a list without repeats"	
for key, value in glossary.items():
	print(key.title()+":\n\t"+value+"\n")	