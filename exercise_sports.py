#Write a function that takes in the name of the city and team.

def sport(city, team):
	print ("The " + team.title() + " are from " + city.title() + ".")

sport(team="Blazers", city="Portland")
sport("Portland", "Timbers")
sport(team="Cardinals", city="Stanford")
