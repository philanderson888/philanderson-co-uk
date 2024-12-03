date = "Monday 25/07/22"
print(date)

customer_29 = {
    "first name": "David",
    "last name": "Elliot",
    "address": "4803 Wellesley St.",
    "discounts": ["standard", "volume", "loyalty", "brother-in-law"], 
}

if "brother-in-law" in customer_29["discounts"]:
    discount_amount = .30
elif "loyalty" in customer_29["discounts"]:
    discount_amount = .15
elif "volume" in customer_29["discounts"]:
    discount_amount = .10
elif "standard" in customer_29["discounts"]:
    discount_amount = .05

print("Customer 29's discount is " + str(discount_amount))

# Monday 25/07/22
# Customer 29's discount is 0.3