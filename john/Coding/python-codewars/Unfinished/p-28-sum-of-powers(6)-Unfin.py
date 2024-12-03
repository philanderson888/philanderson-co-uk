# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 89  The next number in having this property is 135

# Task

#We need a function to collect these numbers, that may receive two integers 𝑎 , 𝑏 that defines the 
# 
# range [𝑎 ,𝑏 ] (inclusive) 
# 
# outputs a list of the sorted numbers in the range that fulfills the property described above.

# Examples

# 1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
# If there are no numbers of this kind in the range [a,b] the function should output an empty list.

# input a, b

def sum_dig_pow(a, b):
# for each number in range [a,b] inclusive

    abRange = range(a, (b + 1))

# convert number into string   
# split string into individual characters
# for each character
# convert to an integer

# raise to power of the (index + 1)
    p = 1
    newArray = []
    for num in abRange:
        powerNum = num ** p
        

# eg 23 => 2 to power 1 plus 3 to power 2 => 2 + 9 => 11

# compare to number itself ie 23
        if powerNum == num:
            newArray.append[powerNum]

# 11 does not equal 23 so fail

# if pass then add to array of matching numbers
        p += 1
    return newArray
### end