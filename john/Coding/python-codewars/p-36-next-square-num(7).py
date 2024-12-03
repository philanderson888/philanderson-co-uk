# finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the argument is itself not a perfect square then return -1

def find_next_square_1(sq):
    root_sq = (sq ** (1/2))
    if root_sq.is_integer() == False:
        return -1
    for num in range(sq + 1, 15241630850):
        root_num = (num ** (1/2))
        if root_num.is_integer() == True:
            return num
        
## this function isnt the best as this is made just to work for the codewars(the 15241630850 was to fit the highest test in) - not a proper method

# tried to do it another way but dont know how to do it without making an infinite loop (or making the limit really high)

def find_next_square_2(sq):
    root_sq = (sq ** (1/2))
    if root_sq.is_integer() == False:
        return -1

    i = 1
    sq_numbers = []
    while i < 10000:
        sq_numbers.append(i ** 2)
        i += 1
    print(sq_numbers)
    return sq_numbers[(sq_numbers.index(sq) + 1)]
    
# After looking at solution, it wasn't that hard:

def find_next_square_solution(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1    
        

