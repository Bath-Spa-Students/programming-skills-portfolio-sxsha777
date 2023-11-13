'''Write a Python program that uses the elif statement to determine the season based on the
month provided as input.'''

spring=["march", "april"]
summer=["may", "june", "july", "august", "september"]
autumn=["october", "november"]
winter=["december", "january", "february"]

month=input("Enter month: ")
if month in spring:
    print("It is spring season!")
elif month in summer:
    print("It is summer season!")
elif month in autumn:
    print("It is autumn season!")
else:
    print("It is winter season!")