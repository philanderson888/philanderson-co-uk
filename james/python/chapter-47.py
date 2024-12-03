print()
print('Monday 8 August 2022')
print('Python - Chapter 47: Getting information from functions')
print('==============================================')
print()


print('A function can pass info back to the calling code.')
def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    print(tax)
  
print('This calling code passes 2 arguments to the function')
calc_tax(sales_total=101.37, tax_rate=.05)

print()

print('You can replace the print with return to return the info')
def calc_tax(sales_total, tax_rate):
    tax = sales_total * tax_rate
    return tax

# You could do this to make it 2 lines
def calc_tax(sales_total, tax_rate):
    return(sales_total * tax_rate)
print()

print('You rewrite the calling code with a variable to hold the value passed.')
# Now calc_tax is assigned to sales_tax
sales_tax = calc_tax(sales_total=101.37, tax_rate=.05)
print(sales_tax)

print()
print('You could write this in one line')
print(calc_tax(sales_total=101.37, tax_rate=.05))

