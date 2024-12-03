# Saturday 21/5/22
print()
print('Python - Chapter 23: Input, converting strings, numbers')
print('==============================================')
print('Saturday 21 May 2022')
print()

most_popular_cities = ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow"]
print(most_popular_cities)
print()

# Say we have a list of Englands five most populated cities
print('Using input the user can enter something for the code to check/run')
city_to_check = input("Enter the name of a city: ")

print('Whatever the user enters is assigned to city_to_check')
print()

print('You can use int() to print a number')
monthly_income = 2000
monthly_income_as_an_integer = int(monthly_income)
# int is short for integer (fyi)
print(monthly_income_as_an_integer)

print('To convert a number to have decimal places, use float()')
monthly_income_as_a_float = float(monthly_income)
print(monthly_income_as_a_float)

print('To convert a number into a string for concatenation or other reasons, use str()')
min_wage2 = 750
min_wage = str(min_wage2)
print(min_wage)
print()

# Python - Chapter 23: Input, converting strings, numbers
# ==============================================
# Saturday 21 May 2022

# ['London', 'Edinburgh', 'Manchester', 'Birmingham', 'Glasgow']

# Using input the user can enter something for the code to check/run
# Enter the name of a city:

# Whatever the user enters is assigned to city_to_check

# You can use int() to print a number
# 2000
# To convert a number to have decimal places, use float()
# 2000.0
# To convert a number into a string for concatenation or other reasons, use str()
# 750