prompt= "How old are you? "
prompt+="\n enter quit to stop: " 
age=""
flag=True

while flag:     # age != quit:
	age = input(prompt)
	if age== "quit":
		flag=False					#break
	else:
		age = int(age)
		if age<3:
			print("The ticket is free!")
		elif age<12:
			print("YOur ticket costs 1000 yen")
		elif age>0:
			print("Your ticket costs 1500  yen")
		
		