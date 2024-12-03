print()
print('Monday 18 July 2022')
print('Python - Chapter 38: Accessing a dictionary of lists')
print('==============================================')
print()


customer_155 = {
  "first name": "James", 
  "last name": "Anderson", 
  "address": "2203 random address",
  "siblings": ["Hannah", "John", "Philip"],
  "discounts": ["loyalty", "volume", "standard"]
}
print('This is customer_155`s dictionary.')
for key in customer_155:
    print(key, ' : ', customer_155[key])

print()

# customer_155 qualifies for three discounts, standard, volume and loyalty.
# He doesn't qualify for a fourth one, brother-in-law.
# These are the discounts
brother_in_law = .30
loyalty = .15
volume = .10
standard = .5
print(f'{brother_in_law} is brother-in-law discount')
print(f'{loyalty} is loyalty discount')
print(f'{volume} is volume discount')
print(f'{standard} is standard discount')
print()

print('We go through the list of discounts named "discounts".')
print('When we find a discount, the search stops.')
print()

if "brother-in-law" in customer_155["discounts"]:
  discount_amount = .30
elif "loyalty" in customer_155["discounts"]:
    discount_amount = .15
elif "volume" in customer_155["discounts"]:
    discount_amount = .10
elif "standard" in customer_155["discounts"]:
    discount_amount = .5

print('You will see 0.15 because loyalty is the first discount in dictionary that is being tested.')
print(discount_amount)


'''
Monday 18 July 2022
Python - Chapter 38: Accessing a dictionary of lists
==============================================

This is customer_155`s dictionary.
first name  :  James
last name  :  Anderson
address  :  2203 random address
siblings  :  ['Hannah', 'John', 'Philip']
discounts  :  ['loyalty', 'volume', 'standard']

0.3 is brother-in-law discount
0.15 is loyalty discount
0.1 is volume discount
0.5 is standard discount

We go through the list of discounts named "discounts".
When we find a discount, the search stops.

You will see 0.15 because loyalty is the first discount in dictionary that is being tested.
0.15
'''