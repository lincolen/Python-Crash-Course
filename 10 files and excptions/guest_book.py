while(True):
	name = input("please enter your name, to quit enter 'q':  ")
	name=name.strip()
	if name == 'q':
		break
	print("Hello "+name+"! please let me record you in the guest book")
	with open('guest_book.txt', 'a') as file_object:
		file_object.write(name.title()+"\n")
