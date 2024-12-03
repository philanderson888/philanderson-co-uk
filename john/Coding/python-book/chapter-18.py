date = "Saturday 25/06/22"
print(date)

tasks = ["email Frank", "call Sarah", "meet with Zach"]
del tasks[0]
print("tasks when deleting using del is " + str(tasks))

tasks2 = ["email Frank", "call Sarah", "meet with Zach"]
del tasks[1]
# tasks2 is now "email frank" and "meet with Zach"

# you can also use .remove

tasks2.remove("email Frank")
print("tasks when deleting using .remove is " + str(tasks2))

# Saturday 25/06/22
# tasks when deleting using del is ['call Sarah', 'meet with Zach']
# tasks when deleting using .remove is ['call Sarah', 'meet with Zach']