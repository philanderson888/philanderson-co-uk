'''
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.
'''


def is_palindrome(s):
    s = s.casefold()
    f = reversed(s)
    if list(f) == list(s):
        return True
    else:
        return False