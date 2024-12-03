print("")
print("Classes Friday 26/08/22")
print("===========================")
print("creating patients using Patient Class")
print("")

class Patient():
  def __init__(self, last_name):
    self.last_name = last_name

import json

pid4343 = '{"last_name": "Taleb"}'
x = json.loads(pid4343)
pid4344 = {"last_name": "Anand"}
pid4345 = {"last_name": "Lin"}
pid1298 = {"last_name": "Nilsson"}

print("Patient 4343's last name is " + str(x["last_name"]))
print("Patient 4344's last name is " + pid4344["last_name"])
print("Patient 4345's last name is " + pid4345["last_name"])
print("Patient 1298's last name is " + pid1298["last_name"])
