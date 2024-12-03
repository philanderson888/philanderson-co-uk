#14/08/23 17 lines

def my_function():
    print("This is my function")

my_function()

def afunction(fname):
    print(fname + " Anderson")

afunction("James")
afunction("Philip")
afunction("John")

def function1(fname, lname):
    print(fname + " " + lname)

function1("Christa", "Anderson")

def function2(*kids):
    print("The youngest child is " + kids[1])

function2("James", "Hannah", "John")

def function3(child1, child2, child3):
    print("The oldest child is " + child3)

function3(child1 = "Hannah", child2 = "John", child3 = "Philippa")

'''
This is my function
James Anderson
Philip Anderson
John Anderson
Christa Anderson
The youngest child is Hannah
The oldest child is Philippa
'''

#15/08/23 -- lines

def function4(**kid):
    print("Her last name is " + kid["lname"])

function4(fname = "Hannah", lname = "Anderson")

def function5(country = "London"):
    print("My favourite country is " + country)

function5("Wales")
function5("Edinburgh")
function5()
function5("Birmingham")


def function6(x):
    return 5 * x

print(function6(2))
print(function6(3))
print(function6(4))

def tri_resursion(k):
    if (k > 0):
        result = k + tri_resursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRessurection Example")
tri_resursion(6)

'''
Her last name is Anderson
My favourite country is Wales
My favourite country is Edinburgh
My favourite country is London
My favourite country is Birmingham
10
15
20
Ressurection Example
1
3
6
10
15
21
'''