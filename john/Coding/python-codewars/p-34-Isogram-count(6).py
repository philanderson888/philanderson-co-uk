def duplicate_count(text):
    text = text.lower()
    count = 0
    for letter in text:
        letterCount = text.count(letter)
        if letterCount > 1:
            count += 1
            text = text.replace(letter, "")
    return count

# Returns the number of letters that have been repeated in the string eg. abcab = 2 (a and b)