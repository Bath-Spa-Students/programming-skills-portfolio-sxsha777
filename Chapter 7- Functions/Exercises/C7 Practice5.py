'''Write a Python program that defines a function to check whether a given number is prime.'''

def check_prime(x):
    if x>1:
        for i in range(2,x):
             if x%i == 0:
                print(x,"is not a prime number.")
                break
        else:
         print(x,"is a prime number!!")
    else:
        print(x,"is not a prime number.")

x=int(input("Enter a number: "))
check_prime(x)

