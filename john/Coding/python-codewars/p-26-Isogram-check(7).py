def is_isogram(string):
    if string == "": return True
    string = string.lower()

    for char in string:
        letterCount = string.count(char)
        print(letterCount)
        if letterCount > 1:
            return False
    return True