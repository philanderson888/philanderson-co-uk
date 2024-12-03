print()
print('Thursday 26th August 2022')
print("Python - Chapter 64: Retrieving data")
print('===============================================')
print()

print("In the text file, greet.txt, its entire contents are the string 'Hello, world!'")
with open("greet.txt", "w") as f:
    f.write("Hello, world!")

print("To retrieve those contents, we just use 'r' for read instead of 'w' for write.")
with open("greet.txt", "r") as f:
    text_of_file = f.read()

print()    

print('"Hello, world!" is now stored in text_of_file')
print(text_of_file)

'''
Thursday 26th August 2022
Python - Chapter 64: Retrieving data
===============================================

In the text file, greet.txt, its entire contents are the string 'Hello, world!'
To retrieve those contents, we just use 'r' for read instead of 'w' for write.

"Hello, world!" is now stored in text_of_file
Hello, world!
'''