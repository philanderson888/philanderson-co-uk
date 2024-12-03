print('python - Chapter 13 - if statements nested')
print('==============================================')
print('April 2022')
print()

x = "a"
y = "b"
a = "c"
b = "d"
c = "e"
e = "f"
d = "g"
h = "h"
f = "e"
g = 'I'
if (x == y or a == b) and c == d:
    g = h
else:
    e = f
print(f"If ({x} = {y} or {a} = {b}) and {c} = {d}, then {g} is equal to {h}")
print("Another way to write this is using nesting")
if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f
print()
print('When you use nesting, instead of using "and", you just create a new if or elif statement.')
# If the first line if is true, the next 6 lines execute.
# If the first line is false, the next 6 lines are skipped.

# python - Chapter 13 - if statements nested
# ==============================================
# April 2022

# If (a = b or c = d) and e = g, then I is equal to h
# Another way to write this is using nesting

# When you use nesting, instead of using "and", you just create a new if or elif statement.