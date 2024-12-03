#17/08/23

class class1:
    a = 5

print(class1)


class class2:
    b = 5

obj1 = class2()
print(obj1.b)


class class3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("\nMy name and age is.. ")
obj2 = class3("Hannah", 12)
print(obj2.name)
print(obj2.age)


class class4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
print("\nMy name and age is.. ")
obj3 = class4("Hannah", 12)
print(obj3)


class class5:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        print("\nHello, my name is " + self.name)

    def __str__(self):
        return f"{self.age}"
print("\nMy age is ")

obj5 = class5("Hannah", 12)
print(obj5)

obj4 = class5("Hannah", 12)
obj4.func1()