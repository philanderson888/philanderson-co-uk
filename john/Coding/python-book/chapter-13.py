date = "Friday 08/04/22"
print(date)
c = "door"
d = "door"
x = "yellow"
y = "yellow"
h = "hello"
a = "apple"
b = "apple"
f = "farm"
e = "not farm"

if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f

print("if x == y or a == b then " + g + " should be hello. If not then " + e + " should be farm")

# Friday 08/04/22
# if x == y or a == b then hello should be hello. If not then not farm should be farm