def min_max(lst):
    lst.sort()
    min = lst[0]
    lst.sort(reverse=True)
    max = lst[0]
    return [min, max]

# there is literally a command to do this:
# min(lst) = lowest in lst
# max(lst) = highest
# return [min(lst), max(lst)]
    