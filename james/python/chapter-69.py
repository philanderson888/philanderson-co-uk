print()
print('Friday 23 December 2022')
print('Python - Chapter 69: Accessing CSV files')
print('==============================================')
print()

import csv

with open("competitions.csv") as f:
    file_contents = csv.reader(f)
    potter_competitions = []
    for each_line in file_contents:
      print(each_line)
      potter_competitions += each_line

print("This is the csv file")
print(potter_competitions)
print()

print("We already learnt how to find an element in a list:")
print(potter_competitions[4])
print()

print("But to find the index number of an element, you write the element name.")
index_num = potter_competitions.index("e")
print(index_num)
print()

print("If we were to want to know the winner of the competition")
target = input("Enter the name of a competition: ")
index_number_of_target = potter_competitions.index(target)
index_number_of_winner = index_number_of_target + 1
winner = potter_competitions[index_number_of_winner]
print(f"The winner was {winner}")

'''
Friday 23 December 2022
Python - Chapter 69: Accessing CSV files
==============================================

This is the csv file
['Year', 'Event', 'Winner', '1995', 'Best-Kept Lawn', 'None', '1999', 'Gobstones', 'Welch National', '2006', 'World cup', 'Burkina Faso']

We already learnt how to find an element in a list:
Best-Kept Lawn

But to find the index number of an element, you write the element name.
4

If we were to want to know the winner of the competition
Enter the name of a competition: Gobstones
The winner was Welch National
'''