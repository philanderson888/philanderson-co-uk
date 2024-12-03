print("In this list pick one animal.")
animals = ["pig", "eagle", "elephant", "dog", "shark", "crocodile", "moth", "spider"]
print(animals)

print("Answer all these question with yes/no")
q1 = input("Does it have 4 legs? ").lower()
if q1 == "no":
    q2 = input("Is it able to fly? ").lower()
    q3 = input("Is it smaller than a human? (wingspan if eagle) ").lower()
else:
    q2 = input("Is it larger than a human? ").lower()
    if q2 == "yes":
        q3 = input("Is it cold blooded? ").lower()
    else:
        q3 = input("Does this animal have a large tail? ").lower()


if q1 == "yes":
    animals = ["pig", "elephant", "dog", "crocodile"]
    if q2 == "yes":
        animals = ["crocodile", "elephant"]
        if q3 == "yes":
            animals = "crocodile"
            print(f"The animal you are looking for is: {animals}")
            print("")
        if q3 == "no":
            animals = "elephant"
            print(f"The animal you are looking for is: {animals}")
            print("")
    if q2 == "no":   
        animals = ["dog", "pig"]
        if q3 == "no":
            animals = "pig"
            print(f"The animal you are looking for is: {animals}")
            print("")

        if q3 == "yes":
            animals = "dog"
            print(f"The animal you are looking for is: {animals}")
            print("")

elif q1 == "no":
    animals = ["eagle", "shark", "moth", "spider"]
    if q2 == "yes":
        animals = ["eagle", "moth"]
        if q3 == "yes":
            animals = "moth"
            print(f"The animal you are looking for is: {animals}")
            print("")
        if q3 == "no":
            animals = "eagle"
            print(f"The animal you are looking for is: {animals}")
            print("")
    if q2 == "no":
        animals = ["shark, spider"]
        if q3 == "no":
            animals = "shark"
            print(f"The animal you are looking for is: {animals}")
            print("")
        if q3 == "yes":
            animals = "spider"
            print(f"The animal you are looking for is: {animals}")
            print("")
    