#Write a function that takes in a person's name and prints out a greeting of at least 3 lines.

def greeter(name):
#Takes in a name and greets a person.
	print ("Hey, " + name.title() + "!")
	print ("It's great to see you again, " + name.title() + "!")
	print ("How are you doing today, " + name.title() + "?\n")

names = ['Bobbi', 'Henry', 'Mike']
for name in names:
	greeter(name)
