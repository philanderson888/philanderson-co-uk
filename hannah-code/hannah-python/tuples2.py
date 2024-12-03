fruits = ("apple", "strawberry", "banana", "kiwi", "blueberry", "blackberry")

(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
    print(x)

tuple2 = ("yes", "no", "maybe")
for y in range(len(tuple2)):
    print(tuple2[y])

tuple3 = ("a", "b", "c")
z = 0
while z < len(tuple3):
    print(tuple3[z])
    z = z + 1

tuple4 = ("p", "e", "n") #join two tuples
tuple5 = (4, 5, 6)

tuple6 = tuple4 + tuple5
print(tuple6)

tuple10 = ("d", "a", "d")
tuple11 = tuple10 * 2
print(tuple11) #multiply tuple10 by 2

'''
apple
strawberry
['banana', 'kiwi', 'blueberry', 'blackberry']
apple
banana
cherry
yes
no
maybe
a
b
c
('p', 'e', 'n', 4, 5, 6)
('d', 'a', 'd', 'd', 'a', 'd')
'''