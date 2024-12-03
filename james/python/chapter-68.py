print()
print('Friday 23 December 2022')
print('Python - Chapter 68: Reading CSV files')
print('==============================================')
print()

import csv

with open("competitions.csv") as f:
    file_contents = csv.reader(f)

print("The contents of the CSV file returned by the csv.reader function aren't usable yet.")
print("You have to loop through the data in file_contents, line by line, adding each line to a list.")
with open("competitions.csv", "w") as f:
    file_contents = csv.reader(f)
    potter_competitions = []
    for each_line in file_contents:
        potter_competitions += each_line

print(potter_competitions)