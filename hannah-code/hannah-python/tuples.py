thistuple = ("apple", "banana", "cherry")
print(thistuple)

thattuple = tuple(("apple", "banana", "cherry"))
print(len(thattuple)) #how many items in that tuple

mytuple = ("apple",) #need the comma afterwards
print(type(mytuple))

tuple1 = ("apple", "banana", "cherry") #string
tuple2 = (1, 5, 9, 2, 4)               #interger
tuple3 = (True, False, True)           #boolean

print(tuple1)
print(tuple2)
print(tuple3)

tuple5 = (True, "tomato", 1, False, 7)
print(tuple5)

thisstuple = ('apple', 'strawberry', 'lemon')
if 'lemon' in thisstuple:
    print("Yes!, 'Lemon' is in this tuple")
else:
    print("No! 'Lemon' is not in this tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[-1] = "lemon"
x = tuple(y)

print(x)

yestuple = ("apple", "pineapple", "strawberry", "lemon")
y = list(yestuple)
y.append("orange")
yestuple = tuple(y)

print(yestuple)

tupleyes = ("apple", "banana", "cherry")
y = ("orange",)
tupleyes += y
print(tupleyes) #33 lines

tuplee = ("apple", "banana", "blueberry")
y = list(tuplee)
y.remove("banana")
tuplee = tuple(y)

print(tuplee) #38 lines

fruits = ("apple", "shush", "banana")

(green, lime, yellow) = fruits

print(green)
print(lime)
print(yellow) #43 lines

'''
('apple', 'banana', 'cherry')
3
<class 'tuple'>
('apple', 'banana', 'cherry')
(1, 5, 9, 2, 4)
(True, False, True)
(True, 'tomato', 1, False, 7)
Yes!, 'Lemon' is in this tuple
('apple', 'banana', 'lemon')
('apple', 'pineapple', 'strawberry', 'lemon', 'orange')
('apple', 'banana', 'cherry', 'orange')
('apple', 'blueberry')
apple
shush
banana
'''