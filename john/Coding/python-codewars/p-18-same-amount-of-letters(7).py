def xo(s):
    s = str.lower(s)
    xNum = s.count('x')
    oNum = s.count('o')
    if xNum == oNum:
        return True
    else:
        return False
    
## checks if a string has the same amount of 'x's and 'o's (case insensitive)

