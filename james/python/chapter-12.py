print('python - Chapter 12 - Testing sets of condition')
print('==============================================')
print('9 April 2022')
print()

print('You can test for multiple conditions using "and"')
temp = 15
people = 500000
parent = "alum"
if temp > 30 and people < 100000:
    status = "Very crowded outside"

print()
print(f'temp = {temp} and people = {people}' )
print('Using "and" we will put both of these variables in an if statement.')
print('Both conditions have to be met for the if statement to work.')
print()
weight = 356
time = 5.2
age = 35
height = 78
res = "U.K"
if weight > 300 and time < 6 and age > 17 and height > 72:
    status = "Try and recruit him"
print(f"We ran 4 conditions in an if statement, weight (= {weight}), time(= {time}), age(= {age}), height(= {height})")
print('You can also create a test that passes if any condition is met using "or".')
if temp > 30 or people < 515300 or parent == "alum":
    message = "Welcome to Leeds Beach!"

print()

print('You can combine any number of "and" and "or" conditions. These create ambiguties')
if age > 65 or age < 21 and res == "U.K":
    print("Just needed this for no error")

print()

# This can be read in two ways:
# If the person is over 65 or under 21, and is a resident of the UK, its true
# If the person is over 65, and under 21 or a resident of the UK, its true

# You fix this the same way with maths, using brackets
if (age > 65 or age < 21) and res == "U.K":
    print("Just needed this for no error")
    # or
if age > 65 or (age < 21 and res == "U.K"):
    print("Just needed this for no error")

print("If an if statement using 'or' and 'and', if it can be read two ways you use brackets, like maths.")


# python - Chapter 12 - Testing sets of condition
# ==============================================
# 9 April 2022

# You can test for multiple conditions using "and"

# temp = 15 and people = 500000
# Using "and" we will put both of these variables in an if statement.
# Both conditions have to be met for the if statement to work.

# We ran 4 conditions in an if statement, weight (= 356), time(= 5.2), age(= 35), height(= 78)
# You can also create a test that passes if any condition is met using "or".

# You can combine any number of "and" and "or" conditions. These create ambiguties

# If an if statement using 'or' and 'and', if it can be read two ways you use brackets, like maths.