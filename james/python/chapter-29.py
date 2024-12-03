print()
print('Monday 30 May 2022')
print('Python - Chapter 29: Adding items to dictionaries')
print('==============================================')
print()


customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print('If we use the same example - Customer 155, these are the current values')
print(customer_155)
print()

print('You can add a new pair by specifying the key then the value.')
customer_155["middle name"] = "Jeremiah"
print(f'Customer 155`s values now have {customer_155["middle name"]} on the end.')
print(customer_155)

print()

# Now Customer 155's values are
customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address", "city": "London"}

# In the previous chapter, you learnt how to define a dictionary by breaking it down:
customer_155_2 = {
    1: "James",
    "Anderson": 2,
    "address": "2203 random address",
    3: 2
}

print('You can define an empty dictionary by just putting it as {}')
customer_155_3 = {}
print(customer_155_3)
print('Then you can fill it later with keys and values')
customer_155_3[1] = "James"
customer_155_3["Anderson"] = 2
customer_155_3["address"] = "2203 random address"
print()


# Monday 30 May 2022
# Python - Chapter 29: Adding items to dictionaries
# ==============================================

# If we use the same example - Customer 155, these are the current values
# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}

# You can add a new pair by specifying the key then the value.
# Customer 155`s values now have Jeremiah on the end.
# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address', 'middle name': 'Jeremiah'}

# You can define an empty dictionary by just putting it as {}
# {}
# Then you can fill it later with keys and values