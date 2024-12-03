'''
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a 
parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null, 
depending on your language. You may assume the argument is non-negative.
'''


import math
def find_next_square(sq):
    x = math.sqrt(sq)
    if x % 1 == 0:
        return (x + 1) * (x + 1)
    else:
        return -1