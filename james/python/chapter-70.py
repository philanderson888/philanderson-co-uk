print()
print('Saturday 24th December 2022')
print('Python - Chapter 70: Saving CSV files 1')
print('==============================================')
print()

print("You open/create the file")

import csv
with open("file01.txt", "w", newline="") as file01:
    file01.write("This is file01")

print("newline="" is a technical requirement, just needs to be included")
print()

with open("file01.txt", "r") as file01:
    file01 = file01.read()
print(file01)

'''
Saturday 24th December 2022
Python - Chapter 70: Saving CSV files 1
==============================================

You open/create the file
newline= is a technical requirement, just needs to be included

This is file01
'''