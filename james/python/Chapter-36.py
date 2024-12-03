import json

print()
print('Saturday 16 July 2022')
print('Python - Chapter 36: Appending to a list of dictionaries')
print('==============================================')
print()

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}

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
print('This is the original list')

print()

print('To append to the end of the list, we need to know how many dictionaries are in the list first; using len()')
new_family_id = len(family_members)
print(f'There are {new_family_id} members in the list.')
print()

# Key note: If the length of family_id is 1000, the index number for the last dictionary will be 999.
# Then the id number will be 1000 if you start from 1.

new_first_name = "Philippa"
new_last_name = "Anderson"
print('These are the names we will be appending onto the list of dictionaries')
print(new_first_name)
print(new_last_name)
print()

print('You have to make a new dictionary first.')
new_dictionary = {
    "family id" : new_family_id,
    "first name": new_first_name,
    "last name": new_last_name
}
print(new_dictionary)
print()

print('Then append it to the end of the list.')
print('You will now see the sixth dictionary being added on.')
family_members.append(new_dictionary)
print(json.dumps(family_members, indent=2))
print()




'''
Saturday 16 July 2022
Python - Chapter 36: Appending to a list of dictionaries
==============================================

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
This is the original list

To append to the end of the list, we need to know how many dictionaries are in the list first; using len()
There are 5 members in the list.

These are the names we will be appending onto the list of dictionaries
Philippa
Anderson

You have to make a new dictionary first.
{'family id': 5, 'first name': 'Philippa', 'last name': 'Anderson'}

Then append it to the end of the list.
You will now see the sixth dictionary being added on.
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
  },
  {
    "family id": 5,
    "first name": "Philippa",
    "last name": "Anderson"
  }
]
'''