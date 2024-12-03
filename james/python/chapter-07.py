# Friday 8/4/22
    # Chapter 7: Eliminting Math Ambiguity

total = 1 + 3 * 9
# but without using BIDMAS you can get 16, so to make it clearer. Parenthesis(Brackets) come first.
total = 1 + (3 * 4) # = 13
total2 = (1 + 3) * 4 # = 16
print(total)
print("This is the result of 1 + (3 * 4) when using BIDMAS")
print(total2)
print("This is the result of 1 + 3 * 4 without using BIDMAS")
# So in this example
total2 = 2 * 4 * (4 + 2)
# Is it 2 * (4 * 6) = 48
# or (2 * 4) * 4 + 2 = 34

# You can either do the second * 4 before the 2 is added
total2 = ((2 * 4) * 4) + 2 # = 34
# or
total2 = (2 * 4) * (4 + 2) # = 48