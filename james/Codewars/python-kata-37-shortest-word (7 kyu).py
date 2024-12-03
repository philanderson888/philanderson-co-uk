'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''


def find_short(str):
    newerStr = []
    newStr = str.split()
    for word in newStr:
        newerStr.append(len(word))
    print(newerStr)
    return min(newerStr)