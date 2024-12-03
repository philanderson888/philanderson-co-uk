print()
print('Monday 8 August 2022')
print('Python - Chapter 48: Functions as variables')
print('==============================================')
print()


print('A function IS a variable')
def sum(first_number, second_number):
    return first_number + second_number

def subtract(first_number2, second_number2):
    return first_number2 - second_number2

print('This is 2 variables that hold returned info from the function being added together.')
sum_result = sum(1, 2)
subtract_result = subtract(3, 2)
print(sum_result)
print(subtract_result)
overall_result = sum_result + subtract_result
print(f'{sum_result} + {subtract_result} = {overall_result}')

print()

print('This can be shortened by putting the functions in the variables place')
overall_result = sum(1, 2) + subtract(3, 2)
print()

'''
Monday 8 August 2022
Python - Chapter 48: Functions as variables
==============================================

A function IS a variable
This is 2 variables that hold returned info from the function being added together.
3
1
3 + 1 = 4

This can be shortened by putting the functions in the variables place
'''