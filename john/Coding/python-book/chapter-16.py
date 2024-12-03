date = "Saturday 09/04/22"
print(date)

cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]
cities.append("New York")
print("The added on city using '.append' is " + cities[6])

longer_list_of_cities = cities + ["Dubuque", "New Orleans"]
print("The added city by adding on to an existing list is " + longer_list_of_cities[8])

cities.insert(0, "New York")
print("The first city now is " + cities[0])

# to change the city to another city
cities[2] = "Houston"
# an empty list
todays_tasks = []
# to add stuff to an empty list
todays_tasks = todays_tasks + ["Walk dog", "Buy groceries"]

# Saturday 09/04/22
# The added on city using '.append' is New York
# The added city by adding on to an existing list is New Orleans
# The first city now is New York
