#Create a dictionary with a person's name and his or her response to a question: What's your favorite color?
#Print out their answers using a for loop.

answers = {'bob': 'blue', 'rob': 'red', 'yeller': 'yellow'}

print ("The following list shows the answers to the question, 'What's your favorite color?'.")

for name in answers:
	print (name.title() + "'s favorite color is " + answers[name] + '.')

