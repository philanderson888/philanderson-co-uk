'''
Write a function that doubles every second integer in a list, starting from the left.
'''

# I didnt exactly do this myself but I looked at the solutions then tried again without looking as I was very close to solving it the first time.


def double_every_other(lst):
    newLst = []
    for i in range(0, len(lst)):
        if i % 2 != 0:
            newLst.append(lst[i] * 2)
        else:
            newLst.append(lst[i])
    return newLst


# Alternative option I could have done:

def double_every_other(lst):
    for i in range(1, len(lst), 2):
        lst[i] *= 2
    return lst