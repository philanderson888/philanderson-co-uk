a = 5
b = 10
if a < b:
    print("a is 5 and b is 10 so..")
    print("a is bigger than b")


c = 33
d = 33
if c > d:
    print("\nc is 33 and d is 33 so..")
    print("c is greater than d")
elif c == d:
    print("\nc is 33 and d is 33 so..")
    print("c and d are equal")


e = 200
f = 3
if e < f:
    print("\ne is 200 and f is 3 so..")
    print("e is smaller than f")
elif e == f:
    print("\ne is 200 and f is 3 so..")
    print("e is equal to f")
else:   
    print("\ne is 200 and f is 3 so..")
    print("e is bigger than f")



g = 1
h = 3
i = 2
if g < h and h > i:
    print("\nif (g = 1, i = 2, h = 3) and g < h, h > i so..")
    print("both statemnts are true")
else:
    print("one or both statemnts are wrong") #32 lines of code to this point

"""
a is 5 and b is 10 so..
a is bigger than b

c is 33 and d is 33 so..
c and d are equal

e is 200 and f is 3 so..
e is bigger than f

if (g = 1, i = 2, h = 3) and g < h, h > i so..
both statemnts are true
"""