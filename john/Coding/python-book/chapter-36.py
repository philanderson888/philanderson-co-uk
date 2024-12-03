date = "Wednesday 20/07/22"
print(date)

customers = [
    {
        "customer id": 0,
        "first name": "John",
        "last name": "Anderson",       
        "address": "301 Cedar Rd.",
    },
    {
        "customer id": 1,
        "first name": "Ann",
        "last name": "Sattermeyer",       
        "address": "PO Box 1145",
    },
    {
        "customer id": 2,
        "first name": "Jill",
        "last name": "Somers",       
        "address": "3 Main St.",
    },
]
# to check how many dictionaries
new_customer_id = len(customers)
# to add on to a list of dictionaries
new_dictionary = {
    "customer id": new_customer_id,
    "first name": "new_first_name",
    "last name":  "new_last_name",
    "address": "new_address",
}

customers.append(new_dictionary)

def dictionary_function():
    for key, value in new_dictionary.items():
        print(key, ' : ', value)

print("The amount of dictionaries there are are " + str(new_customer_id))
print("The dictionary added on to the list is: ") + dictionary_function() 

# Wednesday 20/07/22
# The amount of dictionaries there are are 3
# The dictionary added on to the list is:
# customer id  :  3
# first name  :  new_first_name
# last name  :  new_last_name
# address  :  new_address



