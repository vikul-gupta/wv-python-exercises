#Create a dictionary with mountain names as keys and elevations (m and ft) as values.
#Loop through the names and elevations in meters using a function to get the elevation in feet.
#Print out just the names, just the elevations (in meters and feet), and both.

highest_mountains = {'Mount Everest': {'elevation': 8848, 'range': 'himalaya'}, 
         	     'K2': {'elevation': 8611, 'range': 'himalaya'},
         	     'Kangchenjunga': {'elevation': 8586, 'range': 'himalaya'},
         	     'Lhotse': {'elevation': 8516, 'range': 'himalaya'},
         	     'Makalu': {'elevation': 8485, 'range': 'himalaya'}}

print ("The following are the names of the 5 tallest mountains in the world.")
for name in highest_mountains:
    print (name)

print ("\nThe following are the elevations in meters of the 5 tallest mountains in the world.")
for name in highest_mountains:
    print (highest_mountains[name]['elevation'])

print ("\nThe following are the ranges containing the 5 tallest mountains in the world.")
for name in highest_mountains:
    print (highest_mountains[name]['range'])

print ("\nThe following are the names, ranges, and elevations of the 5 tallest mountains in the world.")
for name, dic in highest_mountains.items():
    print ("The height of " + name + ", which is in the " + dic['range'].title() + "s, is " + str(dic['elevation']) + " meters.")

