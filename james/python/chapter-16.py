print('Python - Chapter 16: Adding and changing list elements')
print('==============================================')
print('Tuesday 12 April 2022')
print()


cities = ["London", "Manchester", "Liverpool", "Bristol", "Birmingham"]
print(cities)
print('This is a list of cities in the UK')
print()
# Suppose you want to add a six element, this is the code:
cities.append("Leeds")
print(cities)
print('Now we have added "Leeds" onto the end by using .append()')
print('cities[5] is now assigned "Leeds"')
print()

# If your adding a number instead of a string, no quotation marks needed
# scores.append(47)
print('Some other things:')

cities = cities + ["Cambridge", "Sheffield"]
print('You can append using concatenation.')

longer_list_of_cities = cities + ["Cambridge", "Sheffield"]
print('You can add a list onto a list too.')
# You can create an empty list by putting nothing in the brackets
cities2 = []
print('You can create an empty list by putting nothing in the brackets.')
print('You can insert elements anywhere into a list, not just at the end, using .insert().')
cities.insert(2, "Newcastle")
# Here I inserted it into the third place
# The element in the third place (Liverpool) that got replaced moves down to cities[3]

# Python - Chapter 16: Adding and changing list elements
# ==============================================
# Tuesday 12 April 2022

# ['London', 'Manchester', 'Liverpool', 'Bristol', 'Birmingham']
# This is a list of cities in the UK

# ['London', 'Manchester', 'Liverpool', 'Bristol', 'Birmingham', 'Leeds']
# Now we have added "Leeds" onto the end by using .append()
# cities[5] is now assigned "Leeds"

# Some other things:
# You can append using concatenation.
# You can add a list onto a list too.
# You can create an empty list by putting nothing in the brackets.
# You can insert elements anywhere into a list, not just at the end, using .insert().