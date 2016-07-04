#Create a function that adds two numbers together and outputs a sentence with the answer.

def adder_return(num_1, num_2):
	return num_1 + num_2

numbers = {1: 1, 2: 1, 3: 2}
for num_1 in numbers:
	print ("The sum of " + str(num_1) + " and " + str(numbers[num_1]) + " is " + str(adder_return(num_1, numbers[num_1])) + '.')

