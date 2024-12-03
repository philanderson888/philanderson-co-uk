def correct(s):
    for char in s:
        if char == "0":
            s = s.replace("0", "O")
        elif char == "5":
            s = s.replace("5", "S")
        elif char == "1":
            s = s.replace("1", "I")
    print(s)
    return s