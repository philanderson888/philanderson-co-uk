'''
Your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. 
Your xor function should have the behaviour described above, returning true if exactly one of the two 
expressions evaluate to true, false otherwise.
'''

def xor(a,b):
    if a == True and b == True:
        return False
    elif a == True and b != True:
        return True
    elif a == False and b == True:
        return True
    else:
        return False