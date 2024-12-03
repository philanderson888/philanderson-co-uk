date = "Monday 18/07/22"
print(date) 

# keys dont have to be strings, they can be numbers
rankings = {5: "Finland", 2: "Norway", 3: "Sweden", 7:"Iceland"}
second_ranked_country = rankings[2]
print("the second ranked country is " + second_ranked_country)

country_rankings = {"Finland": 5, "Norway": 2, "Sweden": 3, "Iceland": 7}
norway_rank = country_rankings["Norway"]
print("Norways rank is " + str(norway_rank))

# it is better to write it like this:
rankings = {
    5: "Finland",
    2: "Norway", 
    3: "Sweden", 
    7: "Iceland",
}

# Monday 18/07/22
# the second ranked country is Norway
# Norways rank is 2