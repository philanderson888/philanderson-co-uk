def disemvowel(string_):
    e = string_.replace('A', '')
    z = e.replace('a','')
    y = z.replace('E','')
    x = y.replace('e','')
    w = x.replace('I','')
    o = w.replace('i','')
    ko = o.replace('O','')
    mo = ko.replace('o','')
    bo = mo.replace('U','')
    to = bo.replace('u','')
    return to

## definitely an easier way to do this but this was my way
# Solutions:
def disemvowel2(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

## solution 2:
def disemvowel3(string):
    return "".join(c for c in string if c.lower() not in "aeiou")