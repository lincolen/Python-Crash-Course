from collections import OrderedDict


glossary= OrderedDict()
glossary['pyhton'] =  "A programing langauge with simple syntex"
glossary['list'] = "pythons version of an array. used to keep a series of values"
glossary['slice'] = "A partial potrtion of a list"
glossary['tuple'] = "An unwrittble list"
glossary['dictionary'] = "a series of key-values sets"
glossary["set"]="a function that creats a list without repeats"	
for key, value in glossary.items():
	print(key.title()+":\n\t"+value+"\n")	