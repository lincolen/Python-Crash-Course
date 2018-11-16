def city_country(city, country):
	"""formats a country city output"""
	formated_city=city.title()+", "+country.title()
	return formated_city

print(city_country("jerusalem", "israel"))
print(city_country("berlin", "germany"))
print(city_country("nagoya", "japan"))
