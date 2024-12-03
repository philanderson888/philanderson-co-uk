print()
print('Wednesday 27 July 2022')
print('Python - Chapter 46: An unknown number of arguments')
print('==============================================')
print()

print('The results of a football game:')
def display_result(winner, score):
    print("The winner was " + winner)
    print("The score was " + score)

display_result(winner="Liverpool", score="2-0")

print()

print('But say you want to display other information if something happens.')
print('The function can handle optional arguments by using two asteriks before another parameter. (**):')
print()

other_info = {"overtime": "yes", "injuries": "none"}
def display_result(winner, score, **other_info):
    print("The winner was " + winner)
    print("The score was " + score)
    for key, value in other_info.items():
        print(key + ": " + value )
display_result("Liverpool", "2-0", overtime="yes", injuries="none")
print()

print('The two astericks followed by a parameter mean that there may or may not be one or more arguments passed.')
print('It makes the parameter a dictionary')
print()

print('For positional optional arguments, you just put one asterick.')
def display_nums(first_num, second_num, *opt_nums):
    print(first_num, second_num, opt_nums)
display_nums(100, 200, 300, 400, 500)
print()


'''
Wednesday 27 July 2022
Python - Chapter 46: An unknown number of arguments
==============================================

The results of a football game:
The winner was Liverpool
The score was 2-0

But say you want to display other information if something happens.
The function can handle optional arguments by using two asteriks before another parameter. (**):

The winner was Liverpool
The score was 2-0
overtime: yes
injuries: none

The two astericks followed by a parameter mean that there may or may not be one or more arguments passed.   
It makes the parameter a dictionary

For positional optional arguments, you just put one asterick.
100 200 (300, 400, 500)
'''