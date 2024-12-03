print()
print('Saturday 25 June 2022')
print('Python - Chapter 33: Looping through dictionary key-value pairs')
print('==============================================')
print()


customer_155 = {"first name": "James", "last name": "Anderson", "address": "2203 random address"}
print(customer_155)
print()
# # Last chapter we learnt how to loop through dictionary keys (first name , last name, etc)

print('This chapter we are looping through both the key and value.')
print('Its the same as last chapter, just use .items() and do each_key and each_value.')
print()
print('This is all the key and value pairs of customer_155 printed out:')
print()
for each_key, each_value in customer_155.items():
    print("The customer's " + each_key + " is " + each_value)

print()

# Saturday 25 June 2022
# Python - Chapter 33: Looping through dictionary key-value pairs
# ==============================================

# {'first name': 'James', 'last name': 'Anderson', 'address': '2203 random address'}

# This chapter we are looping through both the key and value.
# Its the same as last chapter, just use .items() and do each_key and each_value.

# This is all the key and value pairs of customer_155 printed out:

# The customer's first name is James
# The customer's last name is Anderson
# The customer's address is 2203 random address