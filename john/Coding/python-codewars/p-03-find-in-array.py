def find_needle(haystack):
  
    x = 0
    while x < len(haystack):
        if haystack[x] == "needle":
            return f"found the needle at position {x}"
        x += 1

# for loop much easier    

# not needed but random array: ['standArrow', 'hay', 'moreHay', 'wiseTree', 'stopSign', 'needle', 'abeLincoln', 'Poland', 'captainAmericaSerum']