print()
print('Wednesday 24th August 2022')
print('Python - Chapter 55: More on building a class')
print('===============================================')
print()

print("We need there to be a variable that has the same value as the attribute, last_name")
print("It can be any name you like as long as its legal")
class patient():
    def __init__(self, last_name):
        self.x = last_name

print(patient)
print()

print("But for now we are going to just use last_name as its easier")
class Patient():
    def __init__(self, last_name):
        self.last_name = last_name

print(Patient)

'''
Wednesday 24th August 2022
Python - Chapter 55: More on building a class
===============================================

We need there to be a variable that has the same value as the attribute, last_name
It can be any name you like as long as its legal
<class '__main__.patient'>

But for now we are going to just use last_name as its easier
<class '__main__.Patient'>
'''