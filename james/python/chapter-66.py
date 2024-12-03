print()
print('Thursday 26 October 2022')
print('Python - Chapter 66: Modules')
print('==============================================')
print()

print('A module is basically a file to store seperate or all functions')
print('It takes just one line in your main program to make all the code in a module available')

print()

print('import (File/module name)')

print()

print('Say you have a function in your main program that calculates tax from your main code')
def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    return tax

calc_tax(sales_total=101.37, tax_rate=.05)

print()

print('You place this function in a module')
print('This is the code:')

print()

print('tax_for_this_order = calculations.calc_tax(sales_total=101.37, tax_rate=.05)')
print()

'''
Thursday 26 October 2022
Python - Chapter 66: Modules
==============================================

A module is basically a file to store seperate or all functions
It takes just one line in your main program to make all the code in a module available

import (File/module name)

Say you have a function in your main program that calculates tax from your main code

You place this function in a module
This is the code:

tax_for_this_order = calculations.calc_tax(sales_total=101.37, tax_rate=.05)
'''