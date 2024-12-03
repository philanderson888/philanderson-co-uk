print()
print('Thursday 25th August 2022')
print("Python - Chapter 62: Data files")
print('===============================================')
print()

print("If we put all the things we've done on a computer, when it turns off, it would all be deleted.")
print("This is how to begin to save data processed by python")
# with open("whatever.txt", "w") as file_to_work_with:

print()

print("This line opens the text file whatever.txt if it exists.")
print("If it doesnt exist, Python creates it.")

print("You could open the file without the initial with, opting to close the file yourself.")
# file_to_work_with = open("whatever.txt", "w"):

print("The designation 'whatever.txt' assumes that the file is in the same folder as the Python program.")
print("If it isnt in the same folder, e.g if its in the data subfolder of the Python folder on Windows, you write:")
# with open("data\whatever.txt", "w") as file_to_work_with:
print()

print("On OS(Apple) and Linux, you use a forward slash:")
# with open("data/whatever.txt", "w") as file_to_work_with:

print("The variable file_to_work_with can be anything, as long as its legal.")