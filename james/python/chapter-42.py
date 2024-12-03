print()
print('Thursday 21 July 2022')
print('Python - Chapter 42: Passing functions information')
print('==============================================')
print()

first_number = 2
second_number = 3

def add_numbers():
    first_number = 2
    second_number = 3
    total = first_number + second_number
    print(total)

print('To call a function, you say the function name and then put brackets after. This is function add_numbers():')
print(f'This function does {first_number} + {second_number} which = {first_number + second_number}')
print()

print('The parenthesis dont have to be empty')
print('Now your passing data as well as calling the function')
print('The numbers inside the parenthesis are called arguments')
print()

first_number = 50
second_number = 40

print(f'In this, "first_number" is {first_number}')
print(f'And "second_number" is {second_number}')
print()

print('The variables inside the parenthesis here are called parameters, which hold arguments.')
print(f'This function, add_numbers adds first_number({first_number}) and second_number({second_number})')
def add_numbers(first_number, second_number):
    total = first_number + second_number
    print(total)
add_numbers(50, 40)

print()

print('You can put a variable into the parenthesis too and call it.')
def greet_user(greeting):
    print(greeting)

greeting = "Hello there"
greet_user(greeting)

print()

'''
Thursday 21 July 2022
Python - Chapter 42: Passing functions information
==============================================

To call a function, you say the function name and then put brackets after. This is function add_numbers():  
This function does 2 + 3 which = 5

The parenthesis dont have to be empty
Now your passing data as well as calling the function
The numbers inside the parenthesis are called arguments

In this, "first_number" is 50
And "second_number" is 40

The variables inside the parenthesis here are called parameters, which hold arguments.
This function, add_numbers adds first_number(50) and second_number(40)
90

You can put a variable into the parenthesis too and call it.
Hello there
'''