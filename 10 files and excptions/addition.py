while(True):
	print("\nenter two integers to be added")
	print("enter 'q' at any time to quit")
	first = input("first number: ")
	if first == "q":
		break
	seconed = input("seconed number: ")
	if seconed == "q":
		break
	try:
		first = int(first)
		seconed = int(seconed)
	#except TypeError:
	except ValueError:
		print("one or more of the values you entered was not a valid number")
	else:
		answer = first+seconed
		print("the sum of the numbers you entered is "+str(answer))