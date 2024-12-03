print()
print('Thursday 25th August 2022')
print("Python - Chapter 61: Changing an attribute's value")
print('===============================================')
print() 

class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

james28 = Patient("Anderson", "James", "14")
# Its as easy as this

james28.first_name = "Smith"
print(james28.first_name)
# Here is a method that does the same thing

class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age > 21:
            print("This patient is a minor")
    def change_first_name(self, new_first_name):
        self.first_name = new_first_name

# It doesnt just have self as a parameter, new_first_name is also there.
# This is the calling code
james28.change_first_name("Smith")

