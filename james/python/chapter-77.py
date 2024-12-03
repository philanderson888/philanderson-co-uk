
print()
print('Saturday 31th December 2022')
print('Python - Chapter 77 : Planning for things to go wrong')
print('==============================================')
print()

print("In the last chapter it displayed a message if the file name was not found.")
print("But if you use a while loop you can ask the user again repeatedly they enter a file that is valid.")

while True:
    try:
        file = input("Enter the file you want to open: ")
        with open(file) as file:
            print(file.read())
            break
    except FileNotFoundError:
        print(f"Sorry, {file} not found.")
        print()

# If you enter a file that exists:
'''
Saturday 31th December 2022
Python - Chapter 77 : Planning for things to go wrong
==============================================

In the last chapter it displayed a message if the file name was not found.
But if you use a while loop you can ask the user again repeatedly they enter a file that is valid.
Enter the file you want to open: file02.csv
Date,Name,Age
16th Feb,James,14
29th Dec,John,17

'''

# If you enter a file that doesnt exist:

'''
Saturday 31th December 2022
Python - Chapter 77 : Planning for things to go wrong
==============================================

In the last chapter it displayed a message if the file name was not found.
But if you use a while loop you can ask the user again repeatedly they enter a file that is valid.
Enter the file you want to open: None.csv
Sorry, None.csv not found.

Enter the file you want to open:
'''