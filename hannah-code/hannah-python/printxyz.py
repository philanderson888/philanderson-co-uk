print('Hello, World!')
if 5 > 2:
    print('five is greater than two')
"""
x = 5
y = "Hi Stupid!"

print(x)
print(y)

=========
x = 5
y = "John"

print(x)
print(y)

=============
x = 4
x = "Sally"
print(x)

==========
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

=============
x = 5
y = "James"

print(type(x))
print(type(y))
"""
#=====================================
#capital make a difference
"""
A = 5
a = "sally"

print(A)
print(a)
"""
#=====================================
#multiple values
"""
x = y = z = 'Orange'

print(x)
print(y)
print(z)
"""

"""
lockets = ["cherry", "lemon", "strawberry"]
x, y, z = lockets

print(x)
print(y)
print(z)
"""
#=====================================
"""
x = "Hannah"
y = "AIS"
z = "the best"

print(x, y, z)
"""
#=====================================
# you can also do 'print(x + y + z) but you need spaces after the word
'''
x = 6
y = 2

print(x + y)
'''
#=====================================
'''
x = "awesome"

def myfunc():
    x = "best"
    print("Python is the " + x)

myfunc()
print("Python is " + x)
'''

def myPoop():
    global y
    y = "awesome"

myPoop()

print("My poop is sooo " + y)