def how_much_i_love_you(nb_petals):
    arr = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    
    nb_petals = nb_petals % 6
    if nb_petals == 0:
        nb_petals = 6
    
    for phrase in arr:
        if phrase == arr[nb_petals - 1]:
            return phrase