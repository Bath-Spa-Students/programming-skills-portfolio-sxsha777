'''Write a python program with an if-else statement that displays Speed is normal if the speed
variable is within the range of 24 to 56. If the speed variable's value is outside this range, 
display 'Speed is abnormal'''

speed=int(input("Enter speed: "))
if speed > 24 or speed < 56:
    print("speed is within normal range.")
else:
    print("speed is outside normal range.")