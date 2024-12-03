print()
print('Saturday 25 June 2022')
print('Python - Chapter 32: Looping through dictionary keys')
print('==============================================')
print()

customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(customer_155)
print()

# Last chapter we learnt how to loop through dictionary values (James, Anderson, etc)
# This chapter is looping the dictionary keys (first name , last name, etc)
print('Its the same as last chapter, just instead of .values(), you use .keys()')
print()

print('This is all the keys in customer_155 printed out:')
for each_key in customer_155.keys():
    print(each_key)

print()

# Saturday 25 June 2022
# Python - Chapter 32: Looping through dictionary keys
# ==============================================

# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}

# Its the same as last chapter, just instead of .values(), you use .keys()

# This is all the keys in customer_155 printed out:
# first name
# last name
# address