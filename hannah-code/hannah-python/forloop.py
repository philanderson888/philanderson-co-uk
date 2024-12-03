#14/08/23 - 26 lines

names = ["Joe", "Jam", "Jom"]
for x in names:
    print(x)

for y in "Joey":
    print(y)

'''
fruits = ["apple", "banana", "cherry"] #exit the loop when z is banana
for z in fruits:
    print(z)
    if z == "banana":
      break
'''
fruits = ["apple", "banana", "cherry"] #exit loop just before z is banana
for z in fruits:
    if z == "banana":
        break
    print(z)

for h in range(6):
    print(h)

for g in range(6):
    print(g)
else:
    print("you finished")


adj = ["yes", "no", "maybe"]
fruit = ["apple", "banana", "cherry"]

for o in adj:
    for p in fruit:
        print(o, p)

'''
Joe
Jam
Jom
J
o
e
y
apple
0
1
2
3
4
5
0
1
2
3
4
5
you finished
yes apple
yes banana
yes cherry
no apple
no banana
no cherry
maybe apple
maybe banana
maybe cherry
'''