print('Python - Chapter 19: Popping elements')
print('==============================================')
print('Friday 15 April 2022')
print()

tasks = ["check emails", "call Bob", "meet with Dylan"]
print(tasks)
print('This is a list of tasks')
print()

# Say i just checked my emails and i wanted to add it to a list of completed tasks:
print('If you want to remove something from a list but keep it for another purpose, use ".pop()"')
print('e.g if you want to move an element from one list onto another list')
print("check emails will now be in tasks_completed and not tasks.")
tasks_completed = tasks.pop(0)
print(tasks_completed)
print()

print('the value of the index number in the brackets is what gets popped')
print('tasks[0] is "call Bob", tasks[1] is "meet with Dylan" and tasks_completed is "check emails"')
print()

print('You can pop an element off a list and append it to another list')
#tasks_completed.append(tasks.pop(0))
#print(tasks_completed)
print('You can also do the same but insert it instead of appending it.')
#tasks_completed.insert(2, tasks.pop(0))
#print(tasks_completed)
print()

# Python - Chapter 19: Popping elements
# ==============================================
# Friday 15 April 2022

# ['check emails', 'call Bob', 'meet with Dylan']
# This is a list of tasks

# If you want to remove something from a list but keep it for another purpose, use ".pop()"
# e.g if you want to move an element from one list onto another list
# check emails will now be in tasks_completed and not tasks.
# check emails

# the value of the index number in the brackets is what gets popped
# tasks[0] is "call Bob", tasks[1] is "meet with Dylan" and tasks_completed is "check emails"

# You can pop an element off a list and append it to another list
# You can also do the same but insert it instead of appending it.