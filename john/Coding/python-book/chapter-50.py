date = "Thursday 25/08/22"
print(date)

# Functions within functions

def now_say_it(content):
  print(content)

def say_something():
  what_to_say = "Hi"
  now_say_it(what_to_say)

print("The function inside a function is told to print: ")
say_something()

# Thursday 25/08/22
# The function inside a function is told to print:
# Hi

