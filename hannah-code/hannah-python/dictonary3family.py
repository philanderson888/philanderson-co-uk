#34 words
cakes = {
    "cake1" : {
        "name" : "chocolate",
        "ingredients" : "flour"
        },
    "cake2" : {
        "name" : "blueberry",
        "ingredients" : "eggs"
        },
    "cake3" : {
        "name" : "vanilla",
        "ingredients" : "vanilla extract"
        },
}
print(cakes)

child1 = {
    "name" : "Joe",
    "age"  : 5
}
child2 = {
    "name" : "Joey",
    "age"  : 5
}
child3 = {
    "name" : "Job",
    "age"  : 5
}
family = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(family)
print(family["child2"]["name"])

'''
{'cake1': {'name': 'chocolate', 'ingredients': 'flour'}, 
'cake2': {'name': 'blueberry', 'ingredients': 'eggs'}, 
'cake3': {'name': 'vanilla', 'ingredients': 'vanilla extract'}}
{'child1': {'name': 'Joe', 'age': 5}, 
'child2': {'name': 'Joey', 'age': 5}, 
'child3': {'name': 'Job', 'age': 5}}
Joey
'''