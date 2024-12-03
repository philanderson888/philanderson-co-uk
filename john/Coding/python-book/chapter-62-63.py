print("")
print("Monday 05/09/22")
print("Data files")
print("====================================")
print("")

# To save a word processing document or spreadsheet(data) on python:

with open("chapter-62-greet.txt", "w") as file_to_use:
    file_to_use.write("Hello World")

# This is creating a file and putting the text "Hello World in it. The file automatically closes because of "with".
# If there is an existing file called "greet.txt" already then it will delete everything because of "w" and put the new text 
# You can also use variables:
greeting = "Hello World"
with open("chapter-62-greet.txt", "w") as file:
    file.write(greeting)