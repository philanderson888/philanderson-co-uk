print()
print('Saturday 16 July 2022')
print('Python - Chapter 37: Creating a dictionary of lists')
print('==============================================')
print()

print('To make a list in a dictionary, you just put the value as the list and the key as the name of the list.')
print()
customer_155 = {
  "first name": "James", 
  "last name": "Anderson", 
  "address": "2203 random address",
  "siblings": ["Hannah", "John", "Philip"]
}

for key in customer_155:
    print(key, ' : ', customer_155[key])

print()


'''
Saturday 16 July 2022
Python - Chapter 37: Creating a dictionary of lists
==============================================

To make a list in a dictionary, you just put the value as the list and the key as the name of the list.

first name  :  James
last name  :  Anderson
address  :  2203 random address
siblings  :  ['Hannah', 'John', 'Philip']
'''