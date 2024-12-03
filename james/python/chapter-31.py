print()
print('Saturday 25 June 2022')
print('Python - Chapter 31: Looping through dictionary values')
print('==============================================')
print()

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(customer_155)
print()

print('Lets say you wanted to display all the values in the customer_155 dictionary')
print('You have to type then all out one by one.')
print(customer_155["first name"])
print(customer_155["last name"])
print(customer_155["address"])

print()

print('This works but imagine a much longer dictionary, it would be too long to write them all out.')
print('This is why you use looping with .values()')
print('This is what the code is doing to loop through them all:')
print('for each value in customer_155, print each value')
print()
print('This is all the values in customer_155 printed out:')
print()
for each_value in customer_155.values():
    print (each_value)

print()


# Saturday 25 June 2022
# Python - Chapter 31: Looping through dictionary values
# ==============================================

# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}

# Lets say you wanted to display all the values in the customer_155 dictionary
# You have to type then all out one by one.
# James
# Anderson
# 2203 random address

# This works but imagine a much longer dictionary, it would be too long to write them all out.
# This is why you use looping with .values()
# This is what the code is doing to loop through them all:
# for each value in customer_155, print each value

# This is all the values in customer_155 printed out:

#  James
# Anderson
# 2203 random address
