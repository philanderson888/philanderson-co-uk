def better_than_average(class_points, your_points):
    classNumber = len(class_points)
    sum = 0
    i = 0
    for x in class_points:
        sum += class_points[i]
        i += 1
    classAvg = sum / classNumber
    if your_points > classAvg: return True 
    else: return False 
 
### before i realised the sum function exists : sum()
## classAvg = sum(class_points) / len(class_points)
## return your_points > classAvg
### Third method: .mean()
## import statistics
## classAvg = statistics.mean(class_points)
## return your_points > classAvg