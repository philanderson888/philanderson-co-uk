dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict1["year"] = 2020
print(dict1)

dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict2.update({"year": 2020})
print(dict2)

dict3 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict3["colour"] = "white"
print(dict3)

dict4 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict4.pop("brand") #'.popitem' pops the last item
print(dict4)

dict5 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del dict5["model"]
print(dict5)
dict5.clear()
print(dict5)