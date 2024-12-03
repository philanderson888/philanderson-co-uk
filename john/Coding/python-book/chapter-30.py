date = "Monday 18/07/22"
print(date) 

# you can delete from a dictionary aswell
customer_29 = {"first name": "David", "last name": "Elliot", "address": "4308 Wellesley St."}
del customer_29["address"]
print("the dictionary without the address is " + str(customer_29))
# you can also change stuff in a dictionary
customer_291 = {"first name": "David", "last name": "Elliot", "address": "4308 Wellesley St.", "city": "Toronto"}
customer_291["city"] = "Winipeg"
# The value of "city", Toronto has now changed to Winipeg
print("customer 291's city was changed from Toronto to " + str(customer_291["city"]))

# Monday 18/07/22
# the dictionary without the address is {'first name': 'David', 'last name': 'Elliot'}
# customer 291's city was changed from Toronto to Winipeg