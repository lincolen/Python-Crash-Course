while(True):
	poll = input("\n"+"why do you like programing?: \n"+"to end the program enter 'q' \n ")
	poll = poll.strip()
	if poll == 'q':
		print("see you next time")
		break
	with open('poll.txt', 'a') as file_object:
		file_object.write(poll+"\n")