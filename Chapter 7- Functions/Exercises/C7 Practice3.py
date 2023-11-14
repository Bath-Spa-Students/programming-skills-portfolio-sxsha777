'''Write a Python program that uses a function to check if a given number is prime or not.'''

def prime_no(a):
    if a>1:
        for i in range(2,a):
             if a%i == 0:
                print(a,"is not a prime number.")
                break
        else:
         print(a,"is a prime number!")
    else:
        print(a,"is not a prime number.")

prime_no(7)
prime_no(15)

