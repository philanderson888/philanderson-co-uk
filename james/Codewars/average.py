'''
There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!
'''


def better_than_average(class_points, your_points):  
    sum = 0
    for i in class_points:
        sum += i
        print(sum)
        
    mean = sum / len(class_points)  
    if mean >= your_points:
        return False
    else:
        return True

