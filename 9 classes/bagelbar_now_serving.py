from restaurant import Restaurant

restaurant = Restaurant("beagelbar", "bagels")
restaurant.describe_restaurant()
print("number of customers served: "+str(restaurant.number_served))
restaurant.number_served = 654
print("number of customers served: "+str(restaurant.number_served))
restaurant.set_number_served(784)
print("number of customers served: "+str(restaurant.number_served))
restaurant.increment_number_served(76)
print("number of customers served: "+str(restaurant.number_served))