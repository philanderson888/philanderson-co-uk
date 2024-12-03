print()
print('Tuesday 23th August 2022')
print('Python - Chapter 52: Setting a flag')
print('==============================================')
print()

most_populated_cities = ["London", "Edinburgh", "Manchester", "Birmingham", "Glasgow"]
print("We learnt to use a while loop to keep repeating something until the user stops it or something is recognised.")
print(most_populated_cities)
print()

user_input = ""
while user_input != "ESC":
    user_input = input("Enter a city, or ESC to quit:")
    if user_input != "ESC":
        for a_populated_city in most_populated_cities:
            if user_input == a_populated_city:
                print("It's one of the most populated cities")
                break

print()

print("Im going to modify this code to use a flag.")
keep_looping = True
while keep_looping == True:
    user_input = input("Enter a city, or ESC to quit.")
    if user_input != "ESC":
        for a_populated_city in most_populated_cities:
            if user_input == a_populated_city:
                print("It's one of the most populated cities")
                break
    else:
        keep_looping = False

print()
print("Line 17 says as long as keep_looping says True, keep looping.")
print("Line 24 and 25 say if the user entered Esc, change keep_looping to False, so stop looping.")