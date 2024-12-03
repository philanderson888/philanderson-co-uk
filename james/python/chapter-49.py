print()
print('Wednesday 17th August 2022')
print('Python - Chapter 49: Local vs Global variables')
print('==============================================')
print()

print("There is Global scope and Local scope")
print("A global variable is one you define in the main body")
x = "Hi"

print("A local variable is in a function")
def variable():
    y = "Hi"
y = "Hi"
print("A global variable is recognised anywhere in your codeprint()")
print("If i did:")
print(y)

print()

print("Python doesnt recognise it, you get an error message")
print("but")
print(x)

print()
print("Python recognises")

print("If you write the print statement in the function, it recognises them")
def z(a, b):
    total = a + b
    print(a)
    print(b)
    print(total)

print()

# If this happens
def x_2():
    y = 2
    print(y)

y = 1
x_2()
print(y)

# On line 40 it displays 2, on line 44 it displays 1