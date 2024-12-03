import json

print()
print('Thursday 30 June 2022')
print('Python - Chapter 34: Creating a list of dictionaries')
print('==============================================')
print()

customer_155 = {
  "first name": "James", 
  "last name": "Anderson", 
  "address": "2203 random address"
 }
print(customer_155)
print('This is one dictionary')
print()

print('In times you would need multiple dictionaries')
print('You create a list of five dictionaries, one for each')
print()
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
print(json.dumps(family_members, indent=4))
print()


# Thursday 30 June 2022
# Python - Chapter 33: Creating a list of dictionaries
# ==============================================

# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}
# This is one dictionary

# In times you would need multiple dictionaries
# You create a list of five dictionaries, one for each

# [
#     {
#         "family id": 0,
#         "first name": "Hannah",
#         "last name": "Anderson."
#     },
#     {
#         "family id": 1,
#         "first name": "John",
#         "last name": "Anderson."
#     },
#     {
#         "family id": 2,
#         "first name": "James",
#         "last name": "Anderson."
#     },
#     {
#         "family id": 3,
#         "first name": "Philip",
#         "last name": "Anderson."
#     },
#     {
#         "family id": 4,
#         "first name": "Christa",
#         "last name": "Anderson."
#     }
# ]