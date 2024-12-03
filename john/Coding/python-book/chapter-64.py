print("")
print("Monday 05/09/22")
print("Retrieving Data")
print("====================================")
print("")

# This is to read a file, the difference is there is a 'r' instead of a 'w'
# 'w' is for write and 'r' is for read

with open("chapter-62-greet.txt", "r") as file_to_use:
    text_of_file = file_to_use.read()

print("The text in the file is " + text_of_file)

#
# Monday 05/09/22
# Retrieving Data
# ====================================
# The text in the file is Hello World