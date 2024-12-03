print()
print('Saturday 31th December 2022')
print('Python - Chapter 74 : JSON Files')
print('==============================================')
print()

print("I've learnt how to open and read a regular text file and display it.:")
with open("Hello_world.txt", "w") as x:
    x.write("Hello, World!")

with open("Hello_world.txt", "r") as x:
    text_file = x.read()

print(text_file)
print("")

print("But if I wanted to save a list to a text file, it doesnt work. You can only have strings.")
print("So you use a JSON file ('JavaScript Object Notation').")


import json

letters = ["a", "b", "c"]
with open("letters.json", "w") as json01:
    json.dump(letters, json01)
    print(letters)

print()
print("It works the same way with dictionaries.")
print()

'''

Saturday 31th December 2022
Python - Chapter 74 : JSON Files
==============================================

I've learnt how to open and read a regular text file and display it.:
Hello, World!

But if I wanted to save a list to a text file, it doesnt work. You can only have strings.
So you use a JSON file ('JavaScript Object Notation').
['a', 'b', 'c']

It works the same way with dictionaries.

'''