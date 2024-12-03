date = "Wednesday 13/07/22"
print(date)

city_to_check = "Tucson"

cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]

for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print("The city that you checked using a for loop was on the list of the cleanest cities")
        break

# Wednesday 13/07/22
# The city that you checked using a for loop was on the list of the cleanest cities