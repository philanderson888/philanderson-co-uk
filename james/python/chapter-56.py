print()
print('Wednesday 24th August 2022')
print('Python - Chapter 56: Creating an instance')
print('===============================================')
print()

class Patient():
    def __init__(self, last_name):
        self.last_name = last_name
print(Patient)
print()

print("The only thing that differs in the form of an instance is what the patients put in.")
print("Each sheet has a unique identifier automatically when printed.")
print("This sheets patient ID (unique identifier) is james28")

print()
print("To fill in the blank part, we do this")
james28 = Patient("Anderson")
print(james28)
print()

print("james28 is just a variable, but each patient must have a different identifier.")
print("We can use the class to make as many instances as we need.")
james28 = Patient("Anderson")
james29 = Patient("Smith")
james30 = Patient("Billet")
james31 = Patient("Coles")
print()

print(james28)
print(james29)
print(james30)
print(james31)
print()

print("Or you could create a dictionary")
james28 = {"last name": "Anderson"}
james29 = {"last name": "Smith"}
james30 = {"last name": "Billet"}
james31 = {"last name": "Coles"}
james54 = {"last name": "Ellis"}

print()

'''
Wednesday 24th August 2022
Python - Chapter 56: Creating an instance
===============================================

<class '__main__.Patient'>

The only thing that differs in the form of an instance is what the patients put in.
Each sheet has a unique identifier automatically when printed.
This sheets patient ID (unique identifier) is james28

To fill in the blank part, we do this
<__main__.Patient object at 0x0000019A07084DC0>

james28 is just a variable, but each patient must have a different identifier.
We can use the class to make as many instances as we need.

<__main__.Patient object at 0x0000019A070249D0>
<__main__.Patient object at 0x0000019A07084DC0>
<__main__.Patient object at 0x0000019A07054CA0>
<__main__.Patient object at 0x0000019A070913D0>

Or you could create a dictionary

'''