def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    elif employed == True and vacation == True:
        return False
    elif employed == False and vacation == True:
        return False
    elif employed == False and vacation == False:
        return False

## due to boolean logic could have done:
## return employed and not vacation
## - False + False = False
## - True + False = False
## - False + True = False
## - True + True == True