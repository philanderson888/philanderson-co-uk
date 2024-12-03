print()
print('Friday 22 July 2022')
print('Python - Chapter 44: Assigning a default value to a parameter')
print('==============================================')
print()


def calc_tax(sales_total, tax_rate):
    print(sales_total * tax_rate)
    print(f'This is a function with keyword arguments, the answer of {sales_total} x {tax_rate} is above.')
calc_tax(sales_total = 101.37, tax_rate = .05)
print()

sales_total = 101.37
tax_rate = .04
print('To make something the default value, you declare it when making the function')
print(f'This is a function with one of the parameters as a default value, its {sales_total} x {tax_rate} ')
def calc_tax(sales_total, tax_rate = .04):
    print(sales_total * tax_rate)

calc_tax(sales_total = 101.37)

print()

print('Then you dont need it when you call the function, the tax_rate is already known as 0.4')
print('You can make an empty default parameter')

def print_order(product, color, size, engraving_text=""):
    print(print_order)


