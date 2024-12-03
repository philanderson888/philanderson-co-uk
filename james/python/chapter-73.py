import csv
from lib2to3.pgen2.token import NEWLINE

print()
print('Thursday 29th December 2022')
print('Python - Chapter 73 : Appending rows to CSV files')
print('==============================================')
print()

print("When you use 'a' instead of 'w' or 'r' in the file opening the code, it will append new data.")
print()
with open("file02.csv", "a", newline="") as file02:
    data01 = csv.writer(file02)
    data01.writerow(["15th Dec", "Hannah", "11"])

with open("file02.csv", "r",) as file02:
    data01 = csv.reader(file02, delimiter=",")
    for each_line in data01:
      print(each_line)


print()

'''
Thursday 29th December 2022
Python - Chapter 73 : Appending rows to CSV files
==============================================

When you use 'a' instead of 'w' or 'r' in the file opening the code, it will append new data.

['Date', 'Name', 'Age']
['16th Feb', 'James', '14']
['29th Dec', 'John', '17']
['15th Dec', 'Hannah', '11']

'''