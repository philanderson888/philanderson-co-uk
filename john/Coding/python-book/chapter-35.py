date = "Wednesday 20/07/22"
print(date)

# here is a list of dictionaries
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
# to access dictionary:
dictionary_to_look_in = customers[1]
customer_address = dictionary_to_look_in["address"]
print("the second customer's address is " + customer_address)

# Wednesday 20/07/22
# the second customer's address is PO Box 1145