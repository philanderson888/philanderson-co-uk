date = "Monday 25/07/22"
print(date)

# to put a list in dictionary:
customer_29 = {
    "first name": "David",
    "last name": "Elliot",
    "address": "4803 Wellesley St.",
    "discounts": ["standard", "volume", "loyalty"],
}
print("This is the dictionary with the list: ")

def dictionary_function():
    for key, value in customer_29.items():
        print(key, ' : ', value)

dictionary_function()

# Monday 25/07/22
# This is the dictionary with the list:
# first name  :  David
# last name  :  Elliot
# address  :  4803 Wellesley St.
# discounts  :  ['standard', 'volume', 'loyalty']
