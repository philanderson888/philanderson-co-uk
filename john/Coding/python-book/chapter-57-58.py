print("")
print("Classes Friday 26/08/22")
print("===========================")
print("creating patients using Patient Class")
print("")

# Accessing the class

class Patient():
  def __init__(self, last_name, first_name, age):
    self.last_name = last_name
    self.first_name = first_name
    self.age = age

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Lin", "Lilly", 48)
pid1298 = Patient("Nilsson", "Rhonda", 33)

# To get Sue Taleb's age:
age_of_patient = pid4343.age
# To display it:
print("age of patient is " + str(age_of_patient))

print(f"First patient - {pid4343.first_name} {pid4343.last_name}, age {pid4343.age}") 
print(f"Second patient - {pid4344.first_name} {pid4344.last_name}, age {pid4344.age}")
print(f"Third patient - {pid4345.first_name} {pid4345.last_name}, age {pid4345.age}")
print(f"Fourth patient - {pid1298.first_name} {pid1298.last_name}, age {pid1298.age}")  

