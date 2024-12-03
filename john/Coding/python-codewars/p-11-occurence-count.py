def str_count(strng, letter):
    count = 0
    for x in strng:
        if x == letter:
            count += 1
    return count

## OR do:
## count = strng.count(letter)
## return count