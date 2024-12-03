a = "Hello, World"
print(a[1])

for x in "banana":
    print(x)

#length of string
b = "Bye World!"
print(len(b))

#===============================================================================
txt = "Your the dumbes person ever!"
print("dumbest" in txt)
print("studid" in txt)
if "dumbest" in txt:
    print("Yes! 'Dumbest' is in the text")
else:
    print("No! 'Dumbest' is not in the text")

#===============================================================================
text = "The bets things in life are bad"
print("good" not in txt)
if "bad" not in text:
    print("no! :( sadly 'good' is not in the text")
else:
    print("YES! 'bad' is in the text")

#===============================================================================
c = "Hello, World!"
#print(c[2:7])
#print(c[:7])
#print(c[2:])
print(c[-5:-1])

#===============================================================================
d = "Hello, World!"
print(d.upper())

e = "HeLlO, WORld!"
print(e.lower())

f = "  Hello, World  "
print(f.strip())
#===============================================================================
g = "Hello, World!"
print(g.replace("H", "G"))

#===============================================================================
h = "Hello, World!"
i = h.split(",")
print(i)

#===============================================================================
j = "Hello"
k = "World!"
l = j + " " + k
print(l)

#===============================================================================
age = 15
textt = "My name is Hannah and im {}"
print(textt.format(age))

#===============================================================================
amount = 10
item = 5
price = 5.00
order = "I want to order {} things of item {} for {}."
print(order.format(amount, item, price))
