cars1 = ["BMW", "Mercedes", "Toyota"]
x = cars1[0]
print(x)

cars3 = ["BMW", "Mercedes", "Toyota"]
print("\nBefore.. ")
print(cars3)


cars2 = ["BMW", "Mercedes", "Toyota"]
y = cars2[0] = "Ford"
print("\nAfter.. ")
print(cars2)

cars4 = ["BMW", "Mercedes", "Toyota"]
z = len(cars4)
print("\nThe amount of cars here is.. ")
print(z)

cars5 = ["BMW", "Mercedes", "Toyota"]

print("\nThe cars here are..")
for i in cars5:
    print(i)

cars6 = ["BMW", "Mercedes", "Toyota"]

cars6.append("Ford")
print("\nCars here..")
print(cars6)

cars7 = ["BMW", "Mercedes", "Toyota"]
print("\nI have popped the Toyota")

cars7.pop(2)
print(cars7)

'''
BMW

Before.. 
['BMW', 'Mercedes', 'Toyota']

After.. 
['Ford', 'Mercedes', 'Toyota']

The amount of cars here is.. 
3

The cars here are..
BMW
Mercedes
Toyota

Cars here..
['BMW', 'Mercedes', 'Toyota', 'Ford']

I have popped the Toyota
['BMW', 'Mercedes']
'''