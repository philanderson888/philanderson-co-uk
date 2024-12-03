date = "Wednesday 24/08/22"
print(date)

def give_greeting(greeting, first_name) :
  print(greeting + ", " + first_name)

give_greeting("Hello there", first_name="Al")

# Note: Positional arguments and parameters always come first, keyword parameters without defaults come second, and keyword parameters with defaults come last.

# to access this dictionary with a function:

customers = {
    "JohnOg": {
        "first name": "John",
        "last name": "Ogden",
        "address": "301 Arbor Rd.",
    },
    "ASatter": {
        "first name": "Ann",
        "last name": "Sattermyer",
        "address": "PO Box 1145",
    },
    "Summerjill": {
        "first name": "Jill",
        "last name": "Somers",
        "address": "3 Main St.",
    },
}

def find_something(dict, inner_dict, target) :
  print(dict[inner_dict][target])

print("Using a function to access the dictionary, Summerjill's last name is: ")
find_something(customers, "Summerjill", "last name")

# Wednesday 24/08/22
# Hello there, Al
# Using a function to access the dictionary, Summerjill's last name is:
# Somers