# Wednesday 25/5/22
print()
print('Wednesday 25 May 2022')
print('Python - Chapter 27: Accessing info in dictionaries')
print('==============================================')
print()
#   Accessing info in dictionaries


customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(customer_155)
print('If we use the same example, Customer 155, for this chapter, then there is 5 pairs of information')
print()

# If we wanted to find a piece of information in a list, this is what we would do:
# customer_info = customer_155[1]


print('In a dictionary, you pick out an element by specifying its key.')
print('If you put in "last name", it will print out:')
customer_last_name = customer_155["last name"]
print(customer_last_name)
print()


# Wednesday 25 May 2022
# Python - Chapter 27: Accessing info in dictionaries
# ==============================================

# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}
# If we use the same example, Customer 155, for this chapter, then there is 5 pairs of information

# In a dictionary, you pick out an element by specifying its key.
# If you put in "last name", it will print out:
# Anderson