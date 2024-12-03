def validate_pin(pin):
    if pin.isdigit() == True:
        pinLength = len(pin)
        print(pinLength)
        if pinLength == 4:
            return True 
        elif pinLength == 6: 
            return True
        else:
            return False
    else:
        return False