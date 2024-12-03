print()
print('Friday 23 December 2022')
print('Python - Chapter 67: CSV files')
print('==============================================')
print()

print("Its been a long time (3 months) since I last coded.")

print("CSV files are text only files that are simplified versions of a spreadsheet or database")
print("CSV - Comma Seperated Values")
print("")

print("You begin by importing Pythons built-in csv module:")
import csv

print("")

print("Say you've exported the Excel spreadsheet as competitions.csv")
print("Then read the file")
with open("competitions.csv", "w") as f:
    file_contents = csv.reader(f)
print(file_contents)
print("")
print("This calls the function 'reader' and returns the argument f")

'''
Friday 23 December 2022
Python - Chapter 67: CSV files
==============================================

Its been a long time (3 months) since I last coded.
CSV files are text only files that are simplified versions of a spreadsheet or database
CSV - Comma Seperated Values

You begin by importing Pythons built-in csv module:

Say you've exported the Excel spreadsheet as competitions.csv
Then read the file
<_csv.reader object at 0x0000019C3D1D2520>

This calls the function 'reader' and returns the argument f
'''