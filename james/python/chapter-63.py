from asyncore import write


print()
print('Thursday 26th August 2022')
print("Python - Chapter 63: Storing data")
print('===============================================')
print()

print("This second line stores the string in that file (greet.txt)")
with open("greet.txt", "w") as f:
    f.write("Hello, world!")
print(f)

'''
Thursday 26th August 2022
Python - Chapter 63: Storing data
===============================================

This second line stores the string in that file (greet.txt)
<_io.TextIOWrapper name='greet.txt' mode='w' encoding='cp1252'>
'''