#Create a dictionary to hold info about pets, with at least 3 key-value pairs.
#Use of a for loop to print out statements like "Willie is a dog."

pets = {'ziggy': 'canary', 'willie': 'dog', 'bobby': 'hamster'}

for name in pets:
	print (name.title() + " is a " + pets[name] + ".")

