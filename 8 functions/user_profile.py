def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
    	profile[key] = value
    return profile
    
eliram=build_profile("eliram", "barak", hobby="gameing", age= 23, personality="pessimist")
print(eliram)
for key, value in eliram.items():
	print(key+" : "+str(value))