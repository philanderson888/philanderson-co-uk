import csv

print()
print('Saturday 24th December 2022')
print('Python - Chapter 71: Saving CSV files 2')
print('==============================================')
print()

# "This opens the file and calls the 'writer' function "
print("The delimeter is what is used to seperate the values (Commas, semicolons:, carets^, pipes| etc")
with open("file01.csv", "w", newline="") as file:
    data_handler = csv.writer(file, delimiter=",")

print()

with open("file01.txt", "r") as file01:
    file01 = file01.read()
print(file01)

