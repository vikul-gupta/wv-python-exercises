#Create a function that takes in a person's first and last name and prints out a greeting.

def greeter(first_name, last_name):
#Takes in a first and last name and greets a person.
        print ("Hey, " + first_name.title() + ' ' + last_name.title() + "!")

names = {'Bobbi': 'fischer', 'Henry': 'Kissinger', 'Mike': 'Brown'}
for first_name in names:
        greeter(first_name, names[first_name])

