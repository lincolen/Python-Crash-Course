rivers={"nile" : "egypt", "yorden" : "israel", "amazon" : "south amerika"}
for river, country in rivers.items():
	print(river.title()+" runs through "+country.title())
for river in rivers:
	print(river.title())
for country in rivers.values():
	print(country)
	