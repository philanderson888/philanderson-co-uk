print("")
print("Monday 05/09/22")
print("Appending Data")
print("====================================")
print("")

# This is how to append or add text onto an existing document:

with open("chapter-62-greet.txt", "a") as file_to_use:
    file_to_use.write("\nHave a nice day!")

# the '\n' is a line separator. So now greet.txt is:
# Hello World!
# Have a nice day!

with open("chapter-62-greet.txt", "r") as file_to_use:
    file_text = file_to_use.read()

print("The text in the file now is " + file_text)

# Monday 05/09/22
# Appending Data
# ====================================

# The text in the file now is Hello World
# Have a nice day!