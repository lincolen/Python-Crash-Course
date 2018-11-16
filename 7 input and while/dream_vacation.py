poll_results={}
poll_active=True
while poll_active:
	name= input("what is your name?: ")
	place= input("if you could visit anyplace in the world where would you go: ")
	poll_results[name]=place
	next= input("is there a person after you? yes/no: ")
	if next=="no":
		poll_active=False
for name, place in poll_results.items():
	print("Kuma blasted "+name+" to "+place)
			
	