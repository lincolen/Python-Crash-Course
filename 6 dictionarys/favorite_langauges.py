favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
should_polle=["sol","millia","sarah","phil"]
for name in should_polle:
	if name in favorite_languages.keys():
		print(name.title()+" thank you for taking the poll")
	elif name not in favorite_languages.keys():
		print(name.title()+" would you consider taking the poll")