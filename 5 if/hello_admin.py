users=[]#"admin","hershel","pshoter43","ramraul","bedman"]
if users:
	for user in users:
		if user=="admin":
			print("hello admin, there are urgent matters that require your attention")
		else:
			print("hello "+user)
else:
	print("we need some users stat")			