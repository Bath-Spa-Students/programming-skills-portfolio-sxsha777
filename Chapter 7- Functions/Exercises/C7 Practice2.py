'''Write a Python function that calculates the factorial of a given positive integer using
recursion.'''

def factorial(x):
   if x == 1:
       return x
   else:
       return x*factorial(x-1)

x=13
print("Finding factorial of a number using recursion.")
print("The factorial of", x, ": ", factorial(x))

