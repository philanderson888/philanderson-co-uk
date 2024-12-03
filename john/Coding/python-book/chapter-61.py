print("")
print("Monday 05/09/22")
print("Changing an attribute's value")
print("====================================")
print("")

class Patient:
  def __init__(self, last_name, first_name, age):
    self.last_name = last_name
    self.first_name = first_name
    self.age = age
  def age_check(self):
    if self.age < 21:
      print("This patient is a minor.")
    elif self.age >= 21:
      print("This patient is an adult.(21+)")
  def change_last_name(self, new_last_name):
    self.last_name = new_last_name

pid4343 = Patient("Taleb", "Sue", 61)

# To get her last name:
print("Patient 4343's last name was " + pid4343.last_name)
# This is how to change it
pid4343.last_name = "Ortega"
print("Patient 4343's last name now is " + pid4343.last_name)
# Or you could use a function(lines 19-20)
pid4343.change_last_name("Ortegah")
print("Patient 4343's last name using a function now is " + pid4343.last_name)

#
# Monday 05/09/22
# Changing an attribute's value
# ====================================

# Patient 4343's last name was Taleb
# Patient 4343's last name now is Ortega
# Patient 4343's last name using a function now is Ortegah