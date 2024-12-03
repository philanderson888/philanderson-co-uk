
print()
print('Saturday 31th December 2022')
print('Python - Chapter 76 : Planning for things to go wrong')
print('==============================================')
print()

print("If you ask a user to enter the name of a file, and the one she enters doesnt exist. It will have an error message.")
print()

print("Here's how to give a clearer message than just an error when a file that doesnt exist is entered:")
try:
    file = input("Enter the file you want to open: ")
    with open(file) as user_file:
        print(user_file.read())
except FileNotFoundError:
    print(f"Sorry, {file} could not be found")

# If you enter a file that exists:
'''
Saturday 31th December 2022
Python - Chapter 76 : Planning for things to go wrong
==============================================

If you ask a user to enter the name of a file, and the one she enters doesnt exist. It will have an error message. 

Here's how to give a clearer message than just an error when a file that doesnt exist is entered:
Enter the file you want to open: file02.csv
Date,Name,Age
16th Feb,James,14
29th Dec,John,17

'''

# If you enter a file that doesnt exist:

'''
Saturday 31th December 2022
Python - Chapter 76 : Planning for things to go wrong
==============================================

If you ask a user to enter the name of a file, and the one she enters doesnt exist. It will have an error message. 

Here's how to give a clearer message than just an error when a file that doesnt exist is entered:
Enter the file you want to open: None.txt
Sorry, None.txt could not be found
'''