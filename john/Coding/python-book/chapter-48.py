date = "Thursday 25/08/22"
print(date)

# Condensing code
def calc_tax(sales_total, tax_rate):
  tax = sales_total * tax_rate
  return(tax)

# Instead of writing:
sales_tax = calc_tax(sales_total=101.37, tax_rate=.05)
print("calc tax printed using a variable: " + str(sales_tax))

# Write this:
print("calc tax condensed and printed without a variable: " + str(calc_tax(sales_total=101.37, tax_rate=.05)))

# Another example
def add_numbers(first_number, second_number):
  return first_number + second_number

def subtract_numbers(first_number, second_number):
  return first_number - second_number

# Instead of writing:
result_of_adding = add_numbers(1, 2)
result_of_subtracting = subtract_numbers(3, 2)
sum_of_results = result_of_adding + result_of_subtracting

# You could make it into 1 simple line - Write this:
sum_of_results = add_numbers(1, 2) + subtract_numbers(3, 2)

print("sum of results is " + str(sum_of_results))

# Thursday 25/08/22
# calc tax printed using a variable: 5.0685
# calc tax condensed and printed without a variable: 5.0685
# sum of results is 4