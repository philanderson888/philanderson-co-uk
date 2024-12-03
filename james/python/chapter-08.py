# Friday 8/4/22
    # Chapter 8: Concatenating text strings
from tkinter import N


print ('python - Chapter 8 - Concatenating text strings')
print ('==============================================')
print('8 April 2022')

print("")

# You can combine two text strings together like this
x = "Hello, "
y = "World!"
xy = x + y 
print("The words " + x + "and " + y + " " + "concatenated make " + xy)
# xy = "Hello, World!"
# This is called concatenation

print("")

# You can do a combination of variables and strings
comma = ","
exclam = "!"
xyz = " Hello" + comma + " World" + exclam
print("This was saying" + xyz + " but the comma and exclamation mark were variables." + "\n" + xyz)

a = 2
b = 4

print ("You cant concatenate strings and numbers, without turning the integer into a string")
print ("the sum of " + str(a) + ' + ' + str(a) + " is " + str(b))

# python - Chapter 8 - Concatenating text strings
# ==============================================
# 8 April 2022

# The words Hello, and World! concatenated make Hello, World!

# This was saying Hello, World! but the comma and exclamation mark were variables.
# Hello, World!
# You cant concatenate strings and numbers, without turning the integer into a string
# the sum of 2 + 2 is 4