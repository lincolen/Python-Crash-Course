magicians=["hodini", "gandalf", "dumbledore"]
great_magicians=[]

def make_great(magicianz):
	great_magicians=[]
	"""adds the title great to every magicians name"""
	for magician in magicianz:
		magician="the Great "+magician
		great_magicians.append(magician)	
	return great_magicians
	# magicianz[:]=great_magicians

	
def show_magicians(magicians):
	""" prints every magicians name seperatly"""
	for magician in magicians:
		print(magician.title())

				
def delete(lis):
	while lis:
		del lis[-1]


great_magicians= make_great(magicians[:])

show_magicians(magicians)
show_magicians(great_magicians)