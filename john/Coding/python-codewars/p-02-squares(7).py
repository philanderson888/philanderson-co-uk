def square_digits(num):
    # convert to string
    numAsString = str(num)
    print(" ")
    print("num is " + numAsString)
    
    # split string into individual characters

    n = 0
    stringOfSquares = ""
    while n < len(numAsString):
        nthCharacter = numAsString[n]
        print(f"the {n} character is {nthCharacter}")

    # convert each character back into integer
        nthCharacterInt = int(nthCharacter)

        # square each integer
        nthCharacterSquare = nthCharacterInt * nthCharacterInt

        # convert squared number back into a string
        nthCharacterString = str(nthCharacterSquare)

        # concatenate all the strings
        stringOfSquares += nthCharacterString
        print ("squared number is " + nthCharacterString)
        n += 1

    # output final concatenated string
    print(" ")
    print("full string of squares")
    print("final number: " + stringOfSquares)

    stringOfSquaresAsInteger = int(stringOfSquares)
    return stringOfSquaresAsInteger


square_digits(57342)
