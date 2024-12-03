print()
print('Wednesday 17th August 2022')
print('Python - Chapter 50: Functions with functions')
print('==============================================')
print()

print("You can call a function within a function")
def function1():
    x = "Hi"
    print(x)

print("Or you can break it into 2 functions")
def calling_function():
    print(x)

def function2():
    x = "Hi"
    calling_function()

print()

print("This is an error because x isnt recognised inside the calling_function function. Its a local scope.")
print("You pass the value of function2's x variable to calling_function as an argument")
print("calling_function has to recieve it as a parameter.")

def calling_function(content):
    print(content)

def function2():
    x = "Hi"
    calling_function(x)


