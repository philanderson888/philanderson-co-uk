date = "Wednesday 24/08/22"
print(date)

def calc_tax(sales_total, tax_rate=.04) :
  print(sales_total * tax_rate)

print("The answer to 101.37 * .04 is: ")
calc_tax(sales_total=101.37)


# Note: Only keyword parameters can have a default value. Positional parameters can't.
# Note: Keyword parameters without defaults must come before keyword parameters with defaults.

def print_order(product_name, color, size, engraving_text=" "): 
  print(product_name + color + size + engraving_text)

# Wednesday 24/08/22
# The answer to 101.37 * .04 is:
# 4.0548