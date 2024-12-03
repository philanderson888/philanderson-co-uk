#28 lines
dict1 = {
    "name": "HANNAH",
    "age": 12,
    "school": "ECSFG"
}
for x in dict1: #dict1.keys():
    print(x)

for x in dict1:
    print(dict1[x])
for x in dict1.values():
    print(x)
for x, y in dict1.items():
    print(x, y)


dict2 = {
    "name": "CAP",
    "age": 31,
    "school": "ST ANNES"
}
copydict = dict2.copy()
print(copydict)

dict3 = {
    "name": "CAP",
    "age": 31,
    "school": "ST ANNES"
}
copydict_ = dict(dict3)
print(copydict_)

'''
name
age
school
HANNAH
12
ECSFG
HANNAH
12
ECSFG
name HANNAH
age 12
school ECSFG
{'name': 'CAP', 'age': 31, 'school': 'ST ANNES'}
{'name': 'CAP', 'age': 31, 'school': 'ST ANNES'}
'''