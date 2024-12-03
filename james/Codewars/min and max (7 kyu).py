'''
Write a function that returns both the minimum and maximum number of the given list/array.
'''

def min_max(lst):
    lst.sort()
    if lst[0] < lst[-1]:
        return [lst[0], lst[-1]]
    elif lst[0] == lst[-1]:
        return [lst[0], lst[-1]]
    else:
        return [lst[-1], lst[0]]