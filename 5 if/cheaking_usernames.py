current_users=["albert","eggman","sonic","spiderman"]
new_users=["bender","spiderman","robert","robert"]
for user in new_users:
	if user.lower() in current_users:
		print(user+" please use a diffrent user name")
	else:
		print("wellcome "+user)
		current_users.append(user.lower()) 