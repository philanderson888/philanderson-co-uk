from re import S


date = "Thursday 25/08/22"
print(date)

# Local vs Global variables

# This is a global variable, you can use it anywhere
what_to_say = "Hi"
print("This is a global variable: " + what_to_say)
# A local variable is one in a function, so what_to_say is local here:
def say_something():
  what_to_say = "Hi"
  print("This is a local variable in a function: " + what_to_say)

say_something()
# You cant use the local variable outside of the function.

# Thursday 25/08/22
# This is a global variable: Hi
# This is a local variable in a function: Hi 
