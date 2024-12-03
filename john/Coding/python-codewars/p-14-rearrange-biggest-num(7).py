def descending_order(num):
    if num < 0:
        return "Enter a positive number"
    x = 1
    num = str(num)
    # print(len(num))
    numbers = [num[0]]
    while x < len(num):
        numbers.append(num[x])
     #   print(numbers)
        x += 1
    numbers.sort(reverse=True)
    bigNum = ''.join(numbers)
    bigNum = int(bigNum)
    print(bigNum)
    return bigNum

## takes a positive integer and rearranges it in descending order/biggest possible number
