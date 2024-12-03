print('Python - Chapter 17: Taking slices from lists')
print('==============================================')
print('Thursday 14 April 2022')
print()

cities = ["London", "Manchester", "Liverpool", "Bristol", "Birmingham"]
print(cities)
print('This is a list of cities')
print()
# You can copy elements in the list to create a smaller list
smaller_list_of_cities = cities[1:4]
print(smaller_list_of_cities)
print('This is part of the list "cities", it has been what you called sliced.')
print()

# With this you end up with "Manchester", "Liverpool" and "Bristol" in smaller_list_of_cities

# When you slice from a list, you copy a part of it, not cut
# The first number targets the first element in the slice
# The number after the colon is the index number that comes after the last element in the slice.
# So if you want the last element in the slice to be index number 4, you put 5

# When the first element of the slice is the first element in the list, you can leave out the first number:
smaller_list_of_cities2 = cities[:4]
print(smaller_list_of_cities2)
print('When you dont put anything before the colon, it will just start from the first element in the list')
print()
# When the last element of the slice is the last element in the list, you can leave out the last number
smaller_list_of_cities3 = cities[1:]
print(smaller_list_of_cities3)
print('When you dont put anything after the colon, it will just go to the end of the list')
print()

# Python - Chapter 17: Taking slices from lists
# ==============================================
# Thursday 14 April 2022

# ['London', 'Manchester', 'Liverpool', 'Bristol', 'Birmingham']
# This is a list of cities

# ['Manchester', 'Liverpool', 'Bristol']
# This is part of the list "cities", it has been what you called sliced.

# ['London', 'Manchester', 'Liverpool', 'Bristol']
# When you dont put anything before the colon, it will just start from the first element in the list

# ['Manchester', 'Liverpool', 'Bristol', 'Birmingham']
# When you dont put anything after the colon, it will just go to the end of the list