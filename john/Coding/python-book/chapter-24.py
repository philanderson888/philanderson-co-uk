date = "Thursday 14/07/22"
print(date)

cleanest_cities = ["Cheyenne", "cheyenne", "Santa Fe", "santa fe", "Tucson", "tucson", "Great Falls", "great falls"]
city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls"]
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("Its one of the cleanest cities")

lowercase_city_to_check = city_to_check.lower()

# Thursday 14/07/22
# Enter your city: santa fe
# Its one of the cleanest cities