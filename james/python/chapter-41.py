print()
print('Tuesday 19 July 2022')
print('Python - Chapter 41: Functions')
print('==============================================')
print()

print('A function is a block of code that does the same thing every time you invoke its name.')
print('It saves repetitive coding')
print()

print('If you had this')
first_number = 2
second_number = 3
total = first_number + second_number
print(f'{first_number} + {second_number} = {total}')
print()

print('To make this a function, you use def (function name)():')
print('Then you can just call the function whenever you need to.')
def add_numbers():
    first_number = 2
    second_number = 3
    total = first_number + second_number
    print(f'{first_number} + {second_number} = {total}')
add_numbers()

print()

'''
Tuesday 19 July 2022
Python - Chapter 41: Functions
==============================================

A function is a block of code that does the same thing every time you invoke its name.
It saves repetitive coding

If you had this
2 + 3 = 5

To make this a function, you use def (function name)():
Then you can just call the function whenever you need to.
2 + 3 = 5
'''