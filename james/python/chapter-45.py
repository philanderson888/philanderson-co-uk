print()
print('Monday 25 July 2022')
print('Python - Chapter 45: Mixing positional and keyword arguments')
print('==============================================')
print()


def give_greeting(greeting, first_name):
    print(greeting + ", " + first_name)

print('In this function, the first argument is positional and the second is keyword')
give_greeting("Hello there", first_name="Al")

print()

print('Key things:')
print('Positional arguments must come first - before keyword arguments')
print('Positional arguments have to line up with parameters, the keyword argument cant be in its place.')
print('Keyword arguments that are a default value last.')
print()

def give_greeting(greeting, first_name, nickname=" The Magic Boy"):
    print(greeting + ", " + first_name + nickname)
give_greeting("Hello there", first_name="Al",)

print()

print('Lists and dictionaries can be arguments')
family_members = {
  "X": {
    "first name":"Hannah",
    "last name":"Anderson.",
  },
  "Y": {
    "first name":"John",
    "last name":"Anderson.",
  },
  "Z": {
      "first name": "James",
      "last name": "Anderson"
  },
  "A": {
      "first name": "Philip",
      "last name": "Anderson" 
  },
  "B": {
      "first name": "Christa",
      "last name": "Anderson"
  }
}

print()

print('This will print something from the dictionary')
def find_something(dict, inner_dict, target):
    print(dict[inner_dict][target])
find_something(family_members, "Y", "first name")

print()

'''
Monday 25 July 2022
Python - Chapter 45: Mixing positional and keyword arguments
==============================================

In this function, the first argument is positional and the second is keyword
Hello there, Al

Key things:
Positional arguments must come first - before keyword arguments
Positional arguments have to line up with parameters, the keyword argument cant be in its place.
Keyword arguments that are a default value last.

Hello there, Al The Magic Boy

Lists and dictionaries can be arguments

This will print something from the dictionary
John
'''