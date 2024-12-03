print("Chapter 70-2")
print("+========================")
print()

import csv

with open("chapter-70.csv", "w", newline="") as file02:
    data_handler = csv.writer(file02, delimiter=",")

print("This is the csv file")
print(file02)
print(data_handler)

with open("chapter-70.csv", "r") as file02:
    file_to_read = csv.reader(file02)

print()
print("We already learnt how to find an element in a list:")
print(file_to_read)
