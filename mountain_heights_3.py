#Create a dictionary with mountain names as keys and elevations (m and ft) as values.
#Loop through the names and elevations in meters using a function to get the elevation in feet.
#Print out just the names, just the elevations (in meters and feet), and both.

mtn_m = {'Mount Everest': 8848, 'K2': 8611, 'Kangchenjunga': 8586, 'Lhotse': 8516, 'Makalu': 8485}

def convert_to_feet(arr_without_feet):
	elev_feet = []
	for name, elev_meters in sorted(arr_without_feet.items()):
		elev_feet.append(elev_meters * 3.28)
	return elev_feet

elev_ft = convert_to_feet(mtn_m)
highest_mountains = {}
i = 0
for name in sorted(mtn_m):
	highest_mountains[name] = [mtn_m[name], elev_ft[i]]
	i+=1

print ("The following are the names of the 5 tallest mountains in the world.")
for name in highest_mountains:
	print (name)

print ("\nThe following are the elevations in meters of the 5 tallest mountains in the world.")
for name in highest_mountains:
	print (highest_mountains[name][0])

print ("\nThe following are the elevations in feet of the 5 tallest mountains in the world.")
for name in highest_mountains:
    print (highest_mountains[name][1])

print ("\nThe following are the names and elevations of the 5 tallest mountains in the world.")
for name, elevation in highest_mountains.items():
	print ("The height of " + name + " is " + str(elevation[0]) + " meters, or " + str(elevation[1]) + " feet.")

