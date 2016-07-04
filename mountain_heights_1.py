#Create a dictionary with mountain names as keys and elevations as values.
#Print out just the names, just the elevations, and both.

highest_mountains = {'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586, 'Lhotse': 8516, 'Makalu': 8485}

print ("The following are the names of the 5 tallest mountains in the world.")
for name in highest_mountains:
	print (name)

print ("\nThe following are the elevations of the 5 tallest mountains in the world.")
for name in highest_mountains:
	print (highest_mountains[name])

print ("\nThe following are the names and elevations of the 5 tallest mountains in the world.")
for name, elevation in highest_mountains.items():
	print ("The height of " + name + " is " + str(elevation) + " meters.")

