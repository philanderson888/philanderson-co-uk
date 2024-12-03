print()
print('Wednesday 24th August 2022')
print('Python - Chapter 58: Getting info out of instances')
print('===============================================')
print()   

class Patient():
    def __init__(self, age):
        self.age = age

james28 = Patient("Anderson, James, 14")

print("To access James' age, we do this")
age_of_patient = james28.age
print(age_of_patient)
print()

'''
Wednesday 24th August 2022
Python - Chapter 58: Getting info out of instances
===============================================

To access James' age, we do this
Anderson, James, 14

'''