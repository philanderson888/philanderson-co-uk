print("")
print("Monday 05/09/22")
print("Modules")
print("====================================")
print("")

# A module is for importing one 'chapter' or file into another chapter so you dont have to write the code again.

import chapter66module
tax_for_this_order = chapter66module.calc_tax(sales_total=101.37, tax_rate=.05)
print("importing a function in a module, 101.37/0.05 is " + str(tax_for_this_order))