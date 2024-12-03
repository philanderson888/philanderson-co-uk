import json

print()
print('Saturday 31th December 2022')
print('Python - Chapter 75 : Accessing a JSON file')
print('==============================================')
print()

print("If you want to retrieve a saved json file, you begin by opening the file for reading.")
print("Then you call the load() function, specifying the handle to the json file.")
print()

with open("letters.json") as json01:
    letters = json.load(json01)
    print(letters)

'''
Saturday 31th December 2022
Python - Chapter 75 : Accessing a JSON file
==============================================

If you want to retrieve a saved json file, you begin by opening the file for reading.
Then you call the load() function, specifying the handle to the json file.

['a', 'b', 'c']
'''