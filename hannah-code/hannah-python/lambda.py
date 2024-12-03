x = lambda a: a + 6
print("4 + 6 is.. ")
print(x(4))

y = lambda n, m: m * n
print("\n4 x 5 is.. ")
print(y(4, 5))

def function1(h):
    return lambda p : p * h

lamb = function1(5)
print("\n5 x 5 is.. ")
print(lamb(5))

'''
4 + 6 is.. 
10

4 x 5 is.. 
20

5 x 5 is.. 
25
'''