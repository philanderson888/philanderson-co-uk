import csv
from operator import truediv

print()
print('Thursday 29th December 2022')
print('Python - Chapter 72  : Saving CSV files 3')
print('==============================================')
print()

with open("file02.csv", "w") as file01:
    file01.write("")


print("We write some rows of data using x.writerow([])")
print("Opening a file to write overwrites all existing data in the file.")
with open("file02.csv", "w", newline="") as file02:
    data = csv.writer(file02, delimiter=",")
    data.writerow(["Date", "Name", "Age"])
    data.writerow(["16th Feb", "James", "14"])
    data.writerow(["29th Dec", "John", "17"])


with open("file02.csv",) as file02:
    data_02 = csv.reader(file02)
    for each_line in data_02:
      print(each_line)
print()


'''

Thursday 29th December 2022
Python - Chapter 72  : Saving CSV files 3
==============================================

We write some rows of data using x.writerow([])
['Date', 'Name', 'Age']
['16th Feb', 'James', '14']
['29th Dec', 'John', '17']

'''