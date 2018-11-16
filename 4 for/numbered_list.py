#list of numbers from 1 to one million
#numbers=[value+1 for value in range(0,1000000)]
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))
#	for value in range(0, len(numbers)):
#	print(numbers[value])
	
#list of odd umbers between 1 and 20	
#odd_numbers=[value for value in range(1,21,2)]
#for value in range(0,len(odd_numbers)):
#	print(odd_numbers[value])	

#list of cubes from 1 to 10
cubes=[value**3 for value in range(1,11)]
for cube in cubes:
	print(cube)

# list of powers of three until 30
#threes=[value for value in range(3,31,3)]
#for value in range(0,len(threes)):
#	print(threes[value])

#wxample how to make a numbered list without comprinsion 
#loop_numbers=[]
#for value in range(0,1000000):
#	loop_numbers.append(value+1)
#for value in range(0, len(loop_numbers)):
#	print(loop_numbers[value])

print(range(1,4))	