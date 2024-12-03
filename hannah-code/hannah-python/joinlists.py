list1 = ['yes', 'no', 'maybe']
list2 = [2, 5, 3]

list3 = list1 + list2
print(list3)
#============================================================
listy = ["a", "b" , "c"]
listz = [1, 2, 3]

for x in listz:
  listy.append(x)

print(listy)
#============================================================

list10 = ["a", "b" , "c"]
list11 = [1, 2, 3]

list10.extend(list11)
print(list10)