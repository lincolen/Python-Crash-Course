filename = "learning_python.txt"

with open(filename) as file_object:
	contents = file_object.read()
	print(contents.rstrip())
	
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(filename) as file_object:
	learned = file_object.readlines()
for line in learned:
	print(line.strip())

print("")		
for line in learned:
	line = line.replace('python', 'java')
	print(line.strip())
	

	
