print()
print('Python - Chapter 22: for loops nested')
print('==============================================')
print('Saturday 30 April 2022')
print()

first_names = ["James", "John", "Peter", "Andrew", "Matthew"]
last_names = ["Anderson", "Coles", "Parker", "Smith"]
print(first_names)
print(last_names)
print('The first list is of first names')
print('This second list is of last names')
print()

print('In total there could be 20 combinations of names')
print('4 last names for 5 first names')
name1 = "James Anderson"
name2 = "James Coles"
name3 = "James Parker"
name4 = "James Smith"
print(name1)
print(name2)
print(name3)
print(name4)
print()

print('Python can do the repetitive work using nested for loops')
print()
first_names = ["James", "John", "Peter", "Andrew", "Matthew"]
last_names = ["Anderson", "Coles", "Parker", "Smith"]
full_names = []
for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)
    
print(full_names)
print()

# Python - Chapter 22: for loops nested
# ==============================================
# Saturday 30 April 2022

# ['James', 'John', 'Peter', 'Andrew', 'Matthew']
# ['Anderson', 'Coles', 'Parker', 'Smith']
# The first list is of first names
# This second list is of last names

# In total there could be 20 combinations of names
# James Anderson
# James Coles
# James Parker
# James Smith

# Python can do the repetitive work using nested for loops

# ['James Anderson', 'James Coles', 'James Parker', 'James Smith', 'John Anderson', 'John Coles', 'John Parker', 'John Smith', 'Peter Anderson', 'Peter Coles', 'Peter Parker', 'Peter Smith', 'Andrew Anderson', 'Andrew Coles', 'Andrew Parker', 'Andrew Smith', 'Matthew Anderson', 'Matthew Coles', 'Matthew Parker', 'Matthew Smith']