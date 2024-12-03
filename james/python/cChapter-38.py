# Monday 18/7/22
#   Accessing a dictionary of lists

customer_155 = {
  "first name": "James", 
  "last name": "Anderson", 
  "address": "2203 random address",
  "siblings": ["Hannah", "John", "Philip"]
}

# customer_155 qualifies for three discounts, standard, volume and loyalty.
# He doesn't qualify for a fourth one, brother-in-law.
# These are the discounts

# brother-in-law = 30%
# loyalty = 15%
# volume = 10%
# standard - 5%

# We go through the list of discounts named "discounts".
# When we find a discount, the search stops.

if "brother-in-law" in customer_155["discounts"]:
  discount_amount = .30
elif "loyalty" in customer_155["discounts"]:
    discount_amount = .15
elif "volume" in customer_155["discounts"]:
    discount_amount = .10
elif "standard" in customer_155["discounts"]:
    discount_amount = .5

# In this code, the 15% discount is applied because thats the first discount customer_155 has.
# This code introduces the new keyword "in"