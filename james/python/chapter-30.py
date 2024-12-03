print()
print('Saturday 25 June 2022')
print('Python - Chapter 30: Removing and changing dictionary items')
print('==============================================')
print()

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(f'{customer_155} is the dictionary we are using')
print()

# If you remember how to delete an element from a list, its like this:
customer_155_2 = ["James", "Anderson", "address"]
del customer_155_2[0]

print('To delete a key-value pair from a dictionary, you do del customer_155["(key)"]')
print('Here, last name and its value are gone.')
del customer_155["last name"]
print(customer_155)
print()


customer_155[2] = "Smith"
print(f'Here the third value in customer_155 has been changed to {customer_155[2]}')

#or

customer_155["first name"] = "John"
print(f'Also, The value first name has been changed to {customer_155["first name"]}')
print(customer_155)
print()


# Saturday 25 June 2022
# Python - Chapter 30: Removing and changing dictionary items
# ==============================================

# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'} is the dictionary we are 
# using

# To delete a key-value pair from a dictionary, you do del customer_155["(key)"]
# Here, last name and its value are gone.
# {'first name': 'James', 'address': '2203 random address'}

# Here the third value in customer_155 has been changed to Smith
# Also, The value first name has been changed to John
# {'first name': 'John', 'address': '2203 random address', 2: 'Smith'}