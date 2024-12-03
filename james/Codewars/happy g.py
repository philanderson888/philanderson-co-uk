'''
Let's say that "g" is happy in the given string, if there is another "g" immediately to the right or to 
the left of it.

Find out if all "g"s in the given string are happy.
'''

def happy_g(st):
    for i in st:
        i = 0
        while i < len(st):
            if st[i] == "g" and (st[i - 1] or st[i + 1]) == "g":
                return True
            else:
                return False
                i += 1