print()
print('Python - Chapter 21: for loops')
print('==============================================')
print('Saturday 16 April 2022')
print()

city_to_check = "London"

most_popular_cities = ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow"]
print(most_popular_cities)
print('Suppose you want to check ifLondon is in the most_popular_cities list above.')
print(f'One way to do it is put {city_to_check} into an if statement and run it through 5 times to check every element in the list.')
print()

if city_to_check == most_popular_cities[0]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[1]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[2]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[3]:
    print("It's one of the most populated cities")
elif city_to_check == most_popular_cities[4]:
    print("It's one of the most populated cities")

print()

print('But thats a lot of code')
print('Using a for loop is more convenient, it loops through the same steps')
print()

print(f'for a popular city in {most_popular_cities},')
print(f'if {city_to_check} is a popular city, print:')
for popular_city in most_popular_cities:
    if city_to_check == popular_city:
        print("It's one of the most populated cities")

print()

print('This code checks each element one by one.')
print(f'It assigns each element to a variable, then checks the value, if its the value thats being looked for, its assigned to city_to_check which = {city_to_check}')

print()
print('Once Python finds a match, there is no point in continuing the loop, so use break:')
for popular_city in most_popular_cities:
    if city_to_check == popular_city:
        print("It's one of the most populated cities")
        break
print()

# Python - Chapter 21: for loops
# ==============================================
# Saturday 16 April 2022

# ['London', 'Edinburgh', 'Manchester', 'Birmingham', 'Glasgow']
# Suppose you want to check ifLondon is in the most_popular_cities list above.
# One way to do it is put London into an if statement and run it through 5 times to check every element in the list.

# It's one of the most populated cities

# But thats a lot of code
# Using a for loop is more convenient, it loops through the same steps

# for a popular city in ['London', 'Edinburgh', 'Manchester', 'Birmingham', 'Glasgow'],
# if London is a popular city, print:
# It's one of the most populated cities

# This code checks each element one by one.
# It assigns each element to a variable, then checks the value, if its the value thats being looked for, its assigned to city_to_check which = London

# Once Python finds a match, there is no point in continuing the loop, so use break:
# It's one of the most populated cities