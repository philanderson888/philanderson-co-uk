print()
print('Friday 22 July 2022')
print('Python - Chapter 43: Passing functions information differently')
print('==============================================')
print()

print('Before the arguments were positional arguments')
print('They had to be put in order to match the parameter - the first parameter matched with the first argument.')
print()


def add_numbers(first_number, second_number):
    total = first_number + second_number
    print(total)
    print(f'Here first_number is matched with the first argument in add_numbers, {first_number}')
    print(f'and second_number is matched with the second argument, {second_number} - Sum of these make 90')

add_numbers(50,40)
print()

print('But you dont have to make it like this')
print('These are keyword arguments, the order doesnt matter')
print('You just give the value when you call it - e.g - function(brother_name="James") ')
print()

print('This is using keyword arguments, it doesnt matter which order you put the parameters in.')
print()

def names_of_siblings(brother_name, sister_name):
    print("The names of the siblings are " + brother_name + " and " + sister_name)

names_of_siblings(brother_name="James", sister_name="Hannah")

# Python displays: The names of the siblings are James and Hannah.

# If you reverse it, it will be the same
def names_of_siblings(sister_name, brother_name):
    print("The names of the siblings are " + sister_name + " and " + brother_name)

names_of_siblings(sister_name="Hannah", brother_name="James")

'''
Friday 22 July 2022
Python - Chapter 43: Passing functions information differently
==============================================

Before the arguments were positional arguments
They had to be put in order to match the parameter - the first parameter matched with the first argument.   

90
Here first_number is matched with the first argument in add_numbers, 50
and second_number is matched with the second argument, 40 - Sum of these make 90

But you dont have to make it like this
These are keyword arguments, the order doesnt matter
You just give the value when you call it - e.g - function(brother_name="James")

This is using keyword arguments, it doesnt matter which order you put the parameters in.

The names of the siblings are James and Hannah
The names of the siblings are Hannah and James
'''