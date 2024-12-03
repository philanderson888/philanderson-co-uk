print()
print('Thursday 26 May 2022')
print('Python - Chapter 28: The versatility of keys and values')
print('==============================================')
print()


print('In the example we have been using, customer 155, the keys and values are strings.')
customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(customer_155)
print()

print('But the keys dont have to be strings, they can be numbers.')
customer_155_2 = {1: "James", 2: "Anderson", 3: "2203 random address"}

# To pick out a number, you do it like this:
# This would be "Anderson", its not like a list
print('You pick out a value with a integer for a key the same way, just no quotation marks, 2 will print:')
customer_155_23 = customer_155_2[2]
print(customer_155_23)
print('Values can be numbers aswell')
customer_155_3 = {"first name": 1, "last name": 2, "address": 3}
print()
# To pick out a value you do this
customer_155_32 = customer_155_3["last name"]

print('You can mix the numbers any way you want, so you can put the key and value as numbers.')
# When you have a dictionary with a lot of pairs, its easier to break it down.
customer_155_4 = {
    1: "James",
    "Anderson": 2,
    "address": "2203 random address",
    3: 2
}
print(customer_155_4)
print()

# Thursday 26 May 2022
# Python - Chapter 27: The versatility of keys and values
# ==============================================

# In the example we have been using, customer 155, the keys and values are strings.
# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}

# But the keys dont have to be strings, they can be numbers.
# You pick out a value with a integer for a key the same way, just no quotation marks, 2 will print:
# A nderson
# Values can be numbers aswell

# You can mix the numbers any way you want, so you can put the key and value as numbers.
# {1: 'James', 'Anderson': 2, 'address': '2203 random address', 3: 2}