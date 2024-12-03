print()
print('Thursday 26th August 2022')
print("Python - Chapter 65: Appending data")
print('===============================================')
print()

print("To append data to a file while preserving existing data in the file, you use /n (backward slash not forward):")
with open("greet.txt", "a") as f:
    f.write("\nHave a nice day")

print("the /n makes a new line, so the text that follows is placed on a new line.")
# If I write:
with open("greet.txt") as f:
    message = f.read()


print()

print("Python displays")
print(message)
print("'Hello world' and 'Have a nice day' or on seperate lines")

'''
Thursday 26th August 2022
Python - Chapter 65: Appending data
===============================================

To append data to a file while preserving existing data in the file, you use /n (backward slash not forward):      
the /n makes a new line, so the text that follows is placed on a new line.

Python displays:
Hello, world!
Have a nice day
'Hello world' and 'Have a nice day' or on seperate lines

'''