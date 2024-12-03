'''
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
'''


def remove_exclamation_marks(s):
    for i in s:
        if i == "!":
            return s.replace("!", "")
    return s