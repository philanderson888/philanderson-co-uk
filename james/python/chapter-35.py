import json

print()
print('Thursday 14 July 2022')
print('Python - Chapter 35: Accessing a list of dictionaries')
print('==============================================')
print()

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(customer_155)

print('We know how to get information out of a dictionary')
customer_155_first_name = customer_155["first name"]
print(customer_155_first_name)

print('But when we have a list, the dictionaries have no name')
print('Instead they have id`s (Hannah`s index number is 0), but I can give her any family id I want')

family_members = [
  {
    "family id": 0,
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  {
    "family id": 1,
    "first name":"John",
    "last name":"Anderson.",
  },
  {
    "family id": 2,
    "first name":"James",
    "last name":"Anderson.",
  },
  {
    "family id": 3,
    "first name":"Philip",
    "last name":"Anderson.",
  },
  {
    "family id": 4,
    "first name":"Christa",
    "last name":"Anderson.",
  },
]
print(json.dumps(family_members, indent=2))

print('You specify the dictionary first, then you specify the key to get the value printed out')
dictionary_to_look_in = family_members[2]
family_members_address = dictionary_to_look_in["first name"]
print(family_members_address)
print()


'''
Thursday 14 July 2022
Python - Chapter 35: Accessing a list of dictionaries
==============================================

{'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}
We know how to get information out of a dictionary
James
But when we have a list, the dictionaries have no name
Instead they have id`s (Hannah`s index number is 0), but I can give her any family id I want
[
  {
    "family id": 0,
    "first name": "Hannah",
    "last name": "Anderson."
  },
  {
    "family id": 1,
    "first name": "John",
    "last name": "Anderson."
  },
  {
    "family id": 2,
    "first name": "James",
    "last name": "Anderson."
  },
  {
    "family id": 3,
    "first name": "Philip",
    "last name": "Anderson."
  },
  {
    "family id": 4,
    "first name": "Christa",
    "last name": "Anderson."
  }
]
You specify the dictionary first, then you specify the key to get the value printed out
James
'''