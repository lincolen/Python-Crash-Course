oridinal_numbers = list(range(1,11))
print(oridinal_numbers)

for number in oridinal_numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number)+"nd")
	elif number == 3:
		print(str(number) + "rd")
	else:
		print(str(number) + "th")		