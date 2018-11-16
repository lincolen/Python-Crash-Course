cities={
	'nagoya' : {
		'country' : 'japan',
		'population' : "two hundered thousend",
		'fact' : "theres nothing to do in nagoya",
		},
	'vennce' : {
		'country' : "italy",
		'population' : "forty two thousend",
		"fact" : "vennce is slowly sinking",
		},
	'hammburg' : {
		"country" : "germany",
		"population" : "nine thousend",
		'fact' : "the birthplace of the hammburger",
		}, 	 
	}
for city, info in cities.items():
	print("\n"+city.title())
	for category, fact in info.items():
		print(category.title()+": "+fact)