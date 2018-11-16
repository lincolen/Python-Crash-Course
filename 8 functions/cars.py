def make_car(manufacture, model, **info):
	car={}
	car['manufacture']= manufacture
	car['model']= model
	for key, value in info.items():
		car[key]= value
	return car
	
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print( car)