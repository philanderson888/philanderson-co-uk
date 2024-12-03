def feast(beast, dish):
    dishLength = len(dish)
    beastLength = len(beast)
    if dish[0] == beast[0] and dish[dishLength - 1] == beast[beastLength - 1]:
        return True
    else:
        return False
    pass

# Context: each beast has to bring a dish that starts with the first letter of their name and ends with the last letter of their name
