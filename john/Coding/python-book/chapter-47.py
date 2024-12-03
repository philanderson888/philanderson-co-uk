date = "Thursday 25/08/22"
print(date)

# Using a return 
def calc_tax(sales_total, tax_rate) :
  tax = sales_total * tax_rate
  return(tax)

sales_tax = calc_tax(sales_total=101.37, tax_rate=.05)
print("sales tax - (101.37 x 0.05) - is: " + str(sales_tax))

# Thursday 25/08/22
# sales tax - (101.37 x 0.05) - is: 5.0685