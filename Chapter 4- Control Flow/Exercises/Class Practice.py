#if-else loop
'''num=float(input("Enter the number: "))
if num>10:
    num=num-3
else:
    num=num+9
print ("final result: ", num)'''

#nested if-else
age=int(input("Enter your age: "))
height=int(input("Enter your height in cm: "))
if age>16:
    if height>150:
        print("You are eligible to get on this ride.")
    else:
        print("you do not meet the height requirements.")
else:
    print("you are underaged for this ride.")