
print()
print('Tuesday 19 July 2022')
print('Python - Chapter 40: Accessing a dictionary of dictionaries')
print('==============================================')
print()


family_members = {
  "X": {
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  "Y": {
    "first name":"John",
    "last name":"Anderson.",
  },
  "Z": {
      "first name": "James",
      "last name": "Anderson"
  },
  "A": {
      "first name": "Philip",
      "last name": "Anderson" 
  },
  "B": {
      "first name": "Christa",
      "last name": "Anderson"
  }
}

print('Previously we learnt how to find a value in a dictionary by specifying the key')
print(family_members["Y"])
# This prints the whole dictionary of Y

print()

print('To find a specific value in the dictionary, you specify the dictionary and then the key')
print(f'This will print out the first name in the dictionary Y: (which is {family_members["Y"]["first name"]})')
print(family_members["Y"]["first name"])
print()



'''
Tuesday 19 July 2022
Python - Chapter 39: Accessing a dictionary of dictionaries
==============================================

Previously we learnt how to find a value in a dictionary by specifying the key
{'first name': 'John', 'last name': 'Anderson.'}

To find a specific value in the dictionary, you specify the dictionary and then the key
This will print out the first name in the dictionary Y: (which is John)
John
'''