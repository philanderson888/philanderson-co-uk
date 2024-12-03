#10/08/23 22 lines
a = 2
b = 3
c = 4
if a > c or b < c:
    print("(a is 2, b is 3, c = 4) if a > c or b < c..")
    print("Atleast one of the statements is true.")

d = 3
e = 4
if not d > e:
    print("\nthe 'if not' statement means d > e is..")
    print("d is NOT bigger than e")

x = 200
if x > 150:
    print("\nx is bigger than 150")
    if x < 250:
        print("x is smaller than 250!")
else:
    print("x is bigger than 250")

f = 30
g = 40
if g > f:
    pass

'''
(a is 2, b is 3, c = 4) if a > c or b < c..
Atleast one of the statements is true.

the 'if not' statement means d > e is..
d is NOT bigger than e

x is bigger than 150
x is smaller than 250!
'''