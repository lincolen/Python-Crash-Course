eliram={'first_name' : "eliram", 'last_name' : "barak", 'age' : 23, 'city' : "hararit"}
robin={'first_name' : "robin", 'last_name' : "hood", 'age' : "unknown", 'city' : "sherwood"}
jason={'first_name' : "jason", 'last_name' : "lai", 'age' : 22, 'city' : "nagoya"}
persons=[eliram, robin, jason]
for person in persons:
	print("\n"+person["first_name"].title())
	for key in person:
		print(str(key)+": "+str(person[key]).title())
		
dola={"name" : "dola", 'owner' : eliram, "animal" : "cat"}
grace={'name' : "grace", 'owner' : robin, "animel" : "raven"}
rex={'name' : "rex", 'owner' : jason, "animal" : "dog"}
pets=[dola, grace, rex]
for pet in pets:
	print("\n"+pet['name'].title())
	for key, value in pet.items():
			if key== "owner":
				print(key.title()+": "+ value["first_name"].title()+" "+value["last_name"].title())
			else:
				print(key.title()+": "+value.title())	