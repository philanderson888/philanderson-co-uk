print()
print('Sunday 21th August 2022')
print('Python - Chapter 51: While loops')
print('==============================================')
print()

print("A for loop cycles through a series of things, repeating itself until it the series ends or a break.")
print("Example:")
print()

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]
city_to_check = input("Enter the name of a city: ")
print(cleanest_cities)
print(city_to_check)
print()
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("It's one of the cleanest cities")
        break

print()

print("But if the user wants to check cities multiple times;")
print("You use a while loop")
user_input = ""
while user_input != "ESC":
    user_input = input("Enter a city, or ESC to quit:")
    if user_input != "ESC":
        for a_clean_city in cleanest_cities:
            if user_input == a_clean_city:
                print("It's one of the cleanest cities")
                break