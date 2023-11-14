'''Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.'''

largest_no = None
numbers=[]

while True:
    try:
        x = int(input("Enter a number: "))
        if x == 0:
            break
        numbers.append(x)
        if largest_no == None or largest_no < x:
            largest_no=x
    except:
        continue
print(numbers)
print("Largest number is", largest_no)