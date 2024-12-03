import json

print()
print('Monday 18 July 2022')
print('Python - Chapter 39: Creating a dictionary')
print('==============================================')
print()


print('Instead of a list of dictionaries, have a dictionary of dictionaries')
print()
# This is the list of dictionaries we had earlier, there are 5 dictionaries with 3 key-value pairs
family_members = [
  {
    "family id": 0,
    "first name":"Hannah",
    "last name":"Anderson."
  },
  {
    "family id": 1,
    "first name":"John",
    "last name":"Anderson."
  },
  {
    "family id": 2,
    "first name":"James",
    "last name":"Anderson."
  },
  {
    "family id": 3,
    "first name":"Philip",
    "last name":"Anderson."
  },
  {
    "family id": 4,
    "first name":"Christa",
    "last name":"Anderson."
  },
] 
print('A dictionary of dictionaries is made like this, the dictionary name before the curly brackets:')
family_members = {
  0: {
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  1: {
    "first name":"John",
    "last name":"Anderson.",
  },
  2: {
    "first name": "James",
    "last name": "Anderson"
  },
  3: {
    "first name":"Philip",
    "last name":"Anderson."
  },
  4: {
    "first name":"Christa",
    "last name":"Anderson."
  },
}
print(json.dumps(family_members, indent=4))
print()
print('The dictionary names dont have to be numbers though, you can make them any string.')
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
    "first name":"Philip",
    "last name":"Anderson."
  },
  "B": {
    "first name":"Christa",
    "last name":"Anderson."
  },
}


'''
Monday 18 July 2022
Python - Chapter 38: Creating a dictionary
==============================================

Instead of a list of dictionaries, have a dictionary of dictionaries

A dictionary of dictionaries is made like this, the dictionary name before the curly brackets:
{
    "0": {
        "first name": "Hannah",
        "last name": "Anderson."
    },
    "1": {
        "first name": "John",
        "last name": "Anderson."
    },
    "2": {
        "first name": "James",
        "last name": "Anderson"
    },
    "3": {
        "first name": "Philip",
        "last name": "Anderson."
    },
    "4": {
        "first name": "Christa",
        "last name": "Anderson."
    }
}

The dictionary names dont have to be numbers though, you can make them any string.
'''