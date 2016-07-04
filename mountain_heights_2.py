#Create a dictionary with mountain names as keys and elevations as values.
#Print out the names and elevations in alpha order.

highest_mountains = {'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586, 'Lhotse': 8516, 'Makalu': 8485}

for name, elevation in sorted(highest_mountains.items()):
        print ("The height of " + name + " is " + str(elevation) + " meters.")

