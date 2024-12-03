# Programming

# Python

### Adding Strings

python

bool_one = (2 ** 3) == (108 % 100) | ('Cleese' == 'King Arthur')

print ('This means boolean1 is TRUE if either the first item is TRUE or the second item is TRUE.  In this case the FIRST ITEM IS TRUE which makes Boolean1 TRUE')

print ' boolean 1 is ' + str(bool_one)

print 'Anything inside quotes gets printed and it is called a STRING'

print 'to join 2 strings together we use ' + ' the plus symbol + ie A+B=AB'

print 'also can join a string to the answer of a calculation eg 4+3 = ' + str(4+3)

bool_two = True | False

print ' boolean 2 is ' + str(bool_two)

bool_three = ((100**0.5) >= 50) | False

bool_four = True

bool_five = False
```

## If, else and elif statements

```python
def greater_less_equal_5(answer):

if answer > 5:

return 1

elif answer < 5:

return -1

else:

return 0

print greater_less_equal_5(4)

print greater_less_equal_5(5)

print greater_less_equal_5(6)

--------------------------------------------------

# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"

    elif gwrade >= 80:
        return "B"

    elif grade >= 70:
        return "C"

    elif grade >= 65:
        return "D"

    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)
```

## And statements

```python
print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print original
else:
  print "empty"
```

## Counting using range

```jsx
To count from 1 to 1000:

for x in range(1, 1001):
  print(x)

To count from 3 to 10:

for x in range(3, 11)
print(x)
```

## Join Two Words Together  and print them  eg print ('hello' + ' john')

```jsx
print ("hello john")

Answer: 
hello john
```

## Create TWO VARIABLES then JOIN THEM TOGETHER then PRINT THEM eg variable a = 'hello' and variable b = 'john' then print a+b which prints 'hello john'

```jsx
a = "hello"
b = " john"
print(a+b)

Answer:
hello john
```

## Repeat with THREE VARIABLES then THREE NUMBERS ie print (a+b+c) gives firstly HELLO JOHN ANDERSON and then 100 200 300

```jsx
a = "Hello"
b = " John"
c = " Anderson"
print(a + b + c)

d = "100"
e = " 200"
f = " 300"
print(d + e + f)

Answer: 
Hello John Anderson
100 200 300
       
```

## Count Numbers from 1 to 20 all on the same line ie 1,2,3,4,5....20

```jsx
for x in range(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) print(x) 
```