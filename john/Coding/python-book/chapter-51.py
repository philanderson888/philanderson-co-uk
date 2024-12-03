date = "Thursday 25/08/22"
print(date)

# While Loops

# This is a while loop, it checks one thing and sees if its on the list.
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]



# get city from user
user_input = ""
while user_input != "q":
  user_input = input("Enter a city, or q to quit:")
  print(user_input)
  print(cleanest_cities)

  # check user input against list of valid cities
  if user_input != "q":
    match_found = False
  
    # loop over all cities and if match is found set flag to TRUE
    for a_clean_city in cleanest_cities:
      if user_input == a_clean_city:
        match_found = True
        break
    
    # finally, see if we found a MATCH
    print(match_found)
    if match_found == True:
      print("Its one of the cleanest cities.")
    else:
      print("This is not one of the cleanest cities.")


# Thursday 25/08/22
# Enter a city, or q to quit:London
# London
# ['Cheyenne', 'Santa Fe', 'Tucson', 'Great Falls', 'Honolulu']
# False
# This is not one of the cleanest cities.
# Enter a city, or q to quit:Tucson
# Tucson
# ['Cheyenne', 'Santa Fe', 'Tucson', 'Great Falls', 'Honolulu']
# True
# Its one of the cleanest cities.
# Enter a city, or q to quit:q 