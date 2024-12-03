print('python - Chapter 11 - Else and elif statements')
print('==============================================')
print('9 April 2022')

print()

drink = "milk"
print(f'if..else..statement setting drink = {drink}')
if drink == "water":
    print("Yep, its water")
if drink != "water":
    print("Nope, its not water")

print()

print('If a condition is met, something happens, but if the condition isnt met, something also has to happen')
print('Testing if drink is water using `else` statement')
print("Drink is " + drink + "If drink = water, print ' Yep, its water." "If drink isnt (!=) water, print 'Nope, it's not water'")

print()
print (f'drink is {drink} ... let us run this through an else statement')
if drink == "water":
    print("Yep, its water")
else:
    print("Nope, its not water")

print("In if statements the last if is else:")
print ('Finally, there is elif. Its short for "else if". If no test has been successful, elif tries something else.')

if drink == "water":
    print("Yep, its water")
elif drink == "milk":
    print("Oh, its actually milk")
else:
    print("Nope, its not water or milk")

# You can have any number of elif statements.
# You would never have any more than one else statement as its at the end.

# If you dont want to stop testing even after one is successful, you just keep using if.
if drink == "water":
    print("Yep, its water")
if drink == "milk":
    print("Oh, its actually milk")
if drink == "juice":
    print("Nope, its not water or milk")

print()
print("Drink is being tested if it is water, if its not, it tests whether its milk, if its not again, it tests if its juice.")


# python - Chapter 11 - Else and elif statements
# ==============================================
# 9 April 2022

# if..else..statement setting drink = milk
# Nope, its not water

# If a condition is met, something happens, but if the condition isnt met, something also has to happen
# Testing if drink is water using `else` statement
# Drink is milkIf drink = water, print ' Yep, its water.If drink isnt (!=) water, print 'Nope, it's not water'

# drink is milk ... let us run this through an else statement
# Nope, its not water
# In if statements the last if is else:
# Finally, there is elif. Its short for "else if". If no test has been successful, elif tries something else.
# Oh, its actually milk
# Oh, its actually milk

# Drink is being tested if it is water, if its not, it tests whether its milk, if its not again, it tests if its juice.  