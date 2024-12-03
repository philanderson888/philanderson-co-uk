'''
Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language )
that receive a list of integers as input, and return the largest and lowest number in that list, 
respectively.
'''


def minimum(arr):
    arr.sort()
    return arr[0]
        

def maximum(arr):
    arr.sort()
    return arr[-1]