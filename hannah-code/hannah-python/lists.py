mylist = ["apple", "potatoes", "strawberries"]
print(mylist)
print(len(mylist))
print(type(mylist))
print(mylist[2])
print(mylist[0:2])
if "potatoes" in mylist:
    print('Yes! Potatoes is in this list')
else:
    print('No! Potatoes is not in this list')
#==========================================================================

thislist = ['bonbons', 'squashies','crunchie']
thislist[2] = 'maltesers'

print(thislist)
#==========================================================================
thislistt = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislistt[1:3] = ["blackcurrant", "watermelon"]

print(thislistt)

#==========================================================================
thatlist = ['cola', 'dr pepper', 'fanta']
thatlist.insert(2, 'pepsi')
thatlist.append('diet coke')
print(thatlist)
#append is to add on
#insert is to add on to the middle or wherever you put it

#==========================================================================
thoselists = ['carrot', 'watermelon', 'tomatoes']
tropical = ['mango', 'pineapple', 'cocunut']
thoselists.extend(tropical)
thoselists.remove('carrot')
#or ".pop" / ".del"
# ".clear" empties the whole list

print(thoselists)

#==========================================================================
list = ['apple', 'banana', 'cherry']
for x in list:
    print(x)

#==========================================================================
thelist = ["apple", "banana", "cherry"]
i = 0
while i < len(thelist):
  print(thelist[i])
  i = i + 1

#==========================================================================
veggies = ['chocolate', 'vanilla', 'milk', 'blueberry']
newlist = []

for x in veggies:
    if 'l' in x:
        newlist.append(x)
#newlist = [x for x in fruits if "a" in x] (this line of code is the same)

print(newlist)
#==========================================================================

yum = ["apple", "banana", "cherry", "kiwi", "mango"]
newlistt = [x for x in yum if x != "apple"]
#Only accept items that are not "apple"
yum.sort() #ascending
#yum.sort(reverse = True) #descending

print(newlistt)
#==========================================================================

goodlist = [x for x in range(10)]

print(goodlist)
#==========================================================================

def myfuncc(n):
    return abs(n - 50)

whatlist = [100, 65, 83, 46, 93]
whatlist.sort(key = myfuncc)

print(whatlist)
#==========================================================================

yeslist = ['apple', 'Bannanaa', 'Orange', 'kiwi']
yeslist.sort(key = str.lower)

print(yeslist)
