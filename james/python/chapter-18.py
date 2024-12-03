print('Python - Chapter 18: Deleting and removing elements')
print('==============================================')
print('Thursday 14 April 2022')
print()

# Say you have a list of tasks to do
tasks = ["check emails", "call Bob", "meet with Dylan"]
print(tasks)
print('This is a list of tasks')
print()
# tasks[0] is "clean sink"

del tasks[0]
print('To delete elements from a list you do "del (list name[])" ')
print('tasks[0] is now "call Bob", because "check emails was removed"')
print()
print("This is tasks without the first element, clean sink")
print(tasks)
print()

# You can delete any list element by just specifying the index number
del tasks[0]
# tasks[1] is now "meet with Dylan"

print("This is tasks without the second element, call Bob")
print(tasks)
print()

print('An alternate way to remove elements from a list is using (list name).remove()')
tasks.remove("meet with Dylan")
print()

# Python - Chapter 17: Deleting and removing elements
# ==============================================
# Thursday 14 April 2022

# ['check emails', 'call Bob', 'meet with Dylan']
# This is a list of tasks

# To delete elements from a list you do "del (list name[])"
# tasks[0] is now "call Bob", because "check emails was removed"

# This is tasks without the first element, clean sink
# ['call Bob', 'meet with Dylan']

# This is tasks without the second element, call Bob
# ['meet with Dylan']

# An alternate way to remove elements from a list is using (list name).remove()