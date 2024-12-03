print("")
print("Friday 02/09/22")
print("Using methods for functions")
print("====================================")
print("")

# Methods
class Patient:
  def __init__(self, last_name, first_name, age):
    self.last_name = last_name
    self.first_name = first_name
    self.age = age

# function to check if patients are over 21:
  def age_check(self):
    if self.age > 21:
        print(self.first_name + " " + self.last_name + " is not a minor, she is over 21.")
    else:
        print(self.first_name + " " + self.last_name + " is a minor, they are younger than 21.")

pid4343 = Patient("Taleb", "Sue", 61)

# This is a method:
pid4343.age_check()

# Friday 02/09/22
# Using methods for functions
# ====================================

# Sue Taleb is not a minor, she is over 21.