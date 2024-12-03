print()
print('Wednesday 24th August 2022')
print('Python - Chapter 57: A more complex')
print('===============================================')
print()

print("This is a class with a single attribute: last_name")
class Patient():
    def __init__(self, last_name):
        self.last_name = last_name
print(Patient)
print()

print("With instantiated classes 5 times")
james28 = Patient("Anderson")
james29 = Patient("Smith")
james30 = Patient("Billet")
james31 = Patient("Coles")
james54 = Patient("Ellis")
print()

print("We are going to add 2 more attributes")
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
print(Patient)
print()

james28 = Patient("Anderson, James, 14")
james29 = Patient("Smith, John, 14")
james30 = Patient("Billet, Philip, 17")
james31 = Patient("Coles, Hannah, 11")
james54 = Patient("Ellis, Christa, 19")

print("These work like positional arguments, last_name is assigned 'Anderson' for james28")

'''
Wednesday 24th August 2022
Python - Chapter 56: A more complex
===============================================

This is a class with a single attribute: last_name
<class '__main__.Patient'>

With instantiated classes 5 times

We are going to add 2 more attributes
<class '__main__.Patient'>
'''