# Saturday 16/7/22
#   Appending to a list of dictionaries

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
  }
  {
    "family id": 2,
    "first name":"James"
    "last name":"Anderson."
  },
  {
    "family id": 3,
    "first name":"Philip"
    "last name":"Anderson."
  },
  {
    "family id": 4,
    "first name":"Christa"
    "last name":"Anderson."
  },
]


# To add a new family member to the end of the list, we need to know how many dictionaries are in the list first.
# We use len()
new_family_id = len(family_members)

# Key note: If the length of family_id is 1000, the index number for the last dictionary will be 999.
# Then the id number will be 1000 if you start from 1.

new_first_name = "Philippa"
new_last_name = "Anderson"
# To add a new family member to the end of the list, we do this.
new_dictionary = {
    "family id" : new_family_id,
    "first name": new_first_name,
    "last name": new_last_name
}

# Finally, we append this to the end of the list.
family_members.append(new_dictionary)