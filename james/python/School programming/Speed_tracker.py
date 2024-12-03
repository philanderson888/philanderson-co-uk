'''
Speed Tracker: Create a program that takes a time for a car going past a speed camera, 
the time going past the next one and the distance between them to calculate the average speed for the car in mph. 
The cameras are one mile apart. 
'''

time1 = int(input("Enter the time in minutes of the car on the first speed camera:"))
time2 = int(input("Enter the time in minutes of the car on the second speed camera:"))
if time2 <= time1:
    print("Invalid time, the second camera time has to be larger than the first camera time")
    
time = time2 - time1
hours_time = time / 60
multiplier = 1 / hours_time
single_hour = multiplier * hours_time

dist = 1
mph_dist = dist * multiplier
print(str(mph_dist) + "mph")

# Get time of camera1
# Time of camera2
# Take them away and then get time in hours ( / 60)
# Multiply that time by the number needed to get to 1 (1 hour) so ( (1 / time) * time)
    # Create variable for (1 / time) as you multiply the dist by this num after
# Afterwards multiply the dist by (1 / time) to get the miles done for JUST ONE hour

# Overall, make the time into hours, then make it 1 hour by / or *, then use the exact same operation on the dist so dist != 1.
